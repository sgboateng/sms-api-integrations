# SMS API Integration
# Import libraries
import pandas as pd
import requests

import warnings
warnings.filterwarnings("ignore")

def main():

    # Invoke extract CSV function
    df_contacts = contact_list()

    # Check first N records
    # print(df_contacts.head(), '\n')

    # Check data types
    # print(df_contacts.info(), '\n')

    # Invoke send SMS function - Mnotify API
    sms_sender_mnotify_api(df_contacts)

# Create Contact list
def contact_list() -> pd.DataFrame:

    # Contacts list
    contacts = {
    'customer_name': ['Samuel Boateng', 'Kofi Gyebi', 'Nana Baffuor'],
    'account_number': [6090115249, 4090120918, 6090125493],
    'phone_number': [233265682622, 233245785172, 233504100277],
    'expiry_date': ['2026-11-19', '2026-04-01', '2026-09-21']
    }

    # Convert dictionary to Pandas dataframe
    df_contacts = pd.DataFrame(contacts)

    # Convert the 'expiry_date' column to datetime
    df_contacts['expiry_date'] = pd.to_datetime(df_contacts['expiry_date'])

    return df_contacts

# Mnotify API
def sms_sender_mnotify_api(contacts: pd.DataFrame) -> None:

    # API Credentials - LIVE
    api_key = "Qe5F9JMEreFpv2NLvo8enUqR0"
    api_url = "https://api.mnotify.com/api/sms/quick"

    # Headers with API key (if required in headers)
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }

    # Loop through Contacts list
    for irow in contacts.itertuples(index=True, name='Pandas'):

        try:
            # Get recipient details              
            customer_name = getattr(irow, 'customer_name')
            phone_number = getattr(irow, 'phone_number')
            expiry_date = getattr(irow, 'expiry_date').strftime('%B %d, %Y')
            
            # Compose message            
            txt_message = (
                f"Dear {customer_name.title()},\n"
                f"Kindly submit a valid Ghana Card by {expiry_date} for the continued operation of your account.\n"
                f"Zenith Bank...in your best interest."
            )

            # Compose message
            """
            txt_message = (
                f"Dear {customer_name.title()},\n"
                f"Your next loan repayment is due on {expiry_date}.\n"
                f"Zenith Bank...in your best interest."
                )
            """

            # SMS PayLoad
            payload = {
                "recipient": [str(phone_number)],
                "sender": "ZENITHBANK",
                "message": txt_message,
                "is_schedule": False
            }

            # Send the request with TLS 1.2+ and certificate validation
            response = requests.post(
                api_url + '?key=' + api_key,
                json=payload,
                headers=headers,
                verify=True  # Enforces certificate validation using system CA store
            )

            # Print messages
            print(f"[{phone_number}] Status Code:", response.status_code)
            print("Response:", response.text)

        except AttributeError as attr_err:
            print("Missing data in row:", attr_err)
        except requests.exceptions.SSLError as ssl_err:
            print("SSL error:", ssl_err)
        except requests.exceptions.RequestException as req_err:
            print("Error sending SMS:", req_err)

    
		
if __name__ == "__main__":
    main()