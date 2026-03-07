# SMS Sender Class
# Import libraries
import pandas as pd
import requests

import warnings
warnings.filterwarnings("ignore")

# Import Classes
from logger import Logger

# Instantiate Classes
message_logger = Logger()


class SMSNotification:

    # SMS Sender Method - Expiring IDs & Permits
    def send_sms_expiring_ids_permits(self, data_frame: pd.DataFrame) -> None:

        # API Credentials - LIVE
        api_key = "NULQ7NUDmToz23Mb4RaiZqSs4pkXnZxAEGFIERYL"
        gateway_url = "https://internalapis.zenithbank.com.gh/consolidatedMessagingAPI/api/"

        # API Credentials - TEST
        # api_key = "Q7NUDmTozuX5Mb4RaiZqSs4pkXnAEGFI"
        # gateway_url = "https://172.32.254.18/MessagingGateway/api/"

        # Headers with API key (if required in headers)
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        # Loop through dataframe and send SMS to all valid phone numbers
        for irow in data_frame.itertuples(index=True, name='Pandas'):

            try:
                # Get recipient details
                customer_name = getattr(irow, 'CUSTOMERNAME')
                id_type = int(getattr(irow, 'IDENTID'))
                id_expiry_date = getattr(irow, 'IDEXPIRYDATE').strftime('%B %d, %Y')
                phone_number = getattr(irow, 'PHONENUMBER')
                rim_type = getattr(irow, 'RIMTYPE')

                txt_message = str()

                # Match RIM Type and perform required action(s)
                match rim_type:

                    # Individual customer
                    case 'Personal':

                        # Match ID Type and perform required action(s)
                        match id_type:

                            # Residence Permit
                            case 21:
                                
                                # Compose message
                                txt_message = (
                                    f"Dear {customer_name.title()},\n"
                                    f"Kindly submit a valid residence permit by {id_expiry_date} for the continued operation of your account.\n"
                                    f"Zenith Bank...in your best interest."
                                )
                                    
                            # Other IDs
                            case _:

                                # Compose message
                                txt_message = (
                                    f"Dear {customer_name.title()},\n"
                                    f"Kindly submit a valid Ghana Card by {id_expiry_date} for the continued operation of your account.\n"
                                    f"Zenith Bank...in your best interest."
                                )

                    # Corporate Customer
                    case _:

                        # Match ID Type and perform required action(s)
                        match id_type:

                            # Residence Permit
                            case 21:
                                        
                                # Compose message
                                txt_message = (
                                    f"Dear Valued Customer,\n"
                                    f"The residence permits of your signatories/directors are due to expire.\n"
                                    f"Kindly submit valid residence permits for the continued operation of your account.\n"
                                    f"Zenith Bank...in your best interest."
                                )
                                    
                            # Other IDs
                            case _:

                                # Compose message
                                txt_message = (
                                    f"Dear Valued Customer,\n"
                                    f"The IDs of some of your signatories/directors are due to expire.\n"
                                    f"Kindly submit valid Ghana Cards for the continued operation of your account.\n"
                                    f"Zenith Bank...in your best interest."
                                )

                # SMS PayLoad
                payload = {
                    "to": phone_number,
                    "message": txt_message,
                    "campaignType": "Transaction",
                    "channel": "ExpiringIDsPermits"
                }

                # Send the request with TLS 1.2+ and certificate validation
                response = requests.post(
                    gateway_url + 'Sms/Send',
                    json=payload,
                    headers=headers,
                    verify=True  # Enforces certificate validation using system CA store
                )

                print(f"[{phone_number}] Status Code:", response.status_code)
                print("Response:", response.text)

            except AttributeError as attr_err:
                print("Missing data in row:", attr_err)
            except requests.exceptions.SSLError as ssl_err:
                print("SSL error:", ssl_err)
            except requests.exceptions.RequestException as req_err:
                print("Error sending SMS:", req_err)

    # SMS Sender Method - Loan Re-payments
    def send_sms_loan_repayment(self, data_frame: pd.DataFrame) -> None:

        # API Credentials - LIVE
        api_key = "NULQ7NUDmToz23Mb4RaiZqSs4pkXnZxAEGFIERYL"
        gateway_url = "https://internalapis.zenithbank.com.gh/consolidatedMessagingAPI/api/"

        # API Credentials - TEST
        # api_key = "Q7NUDmTozuX5Mb4RaiZqSs4pkXnAEGFI"
        # gateway_url = "https://172.32.254.18/MessagingGateway/api/"

        # Headers with API key (if required in headers)
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        # Loop through dataframe and send SMS to all valid phone numbers
        for irow in data_frame.itertuples(index=True, name='Pandas'):

            try:
                # Get recipient details
                # loan_account = '******' + getattr(irow, 'ACCOUNTNUMBER')[-4:]                
                customer_name = getattr(irow, 'CUSTOMERNAME')          
                next_payment_date = getattr(irow, 'NEXTPMTDATE').strftime('%B %d, %Y')
                phone_number = getattr(irow, 'PHONENUMBER')
                record_count = int(getattr(irow, 'COUNT'))
                
                # Message substring for Email
                msg_substring = "repayments are" if record_count > 1 else "repayment is"

                # Compose message
                txt_message = (
                    f"Dear {customer_name.title()},\n"
                    f"Your next loan {msg_substring} due on {next_payment_date}.\n"
                    f"Zenith Bank...in your best interest."
                )

                # SMS PayLoad
                payload = {
                    "to": phone_number,
                    "message": txt_message,
                    "campaignType": "Transaction",
                    "channel": "LoanRepayments"
                }

                # Send the request with TLS 1.2+ and certificate validation
                response = requests.post(
                    gateway_url + 'Sms/Send',
                    json=payload,
                    headers=headers,
                    verify=True  # Enforces certificate validation using system CA store
                )

                print(f"[{phone_number}] Status Code:", response.status_code)
                print("Response:", response.text)

            except AttributeError as attr_err:
                print("Missing data in row:", attr_err)
            except requests.exceptions.SSLError as ssl_err:
                print("SSL error:", ssl_err)
            except requests.exceptions.RequestException as req_err:
                print("Error sending SMS:", req_err)