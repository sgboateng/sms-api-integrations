# operations/mnotify.py
# Import Libraries
import requests
from typing import List

# Import Warnings
import warnings
warnings.filterwarnings("ignore")

# Import Operations
from operations.shared import SHAREDOperations

# Import Utils
from utils.logger import Logger

# Import Configuations
from config import MNOTIFY_API_KEY, MNOTIFY_API_URL

# Instantiate Operations
shared_ops = SHAREDOperations()

# Instantiate Utils
msg_logger = Logger()


class MNOTIFYOperations():

    # Mnotify API
    def sms_api(self) -> List:

        # Initialize an empty list
        response_list = []

        # Get Contact list
        contacts = shared_ops.contact_list()

        # Headers with API key (if required in headers)
        headers = {
            "X-API-KEY": MNOTIFY_API_KEY,
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
                    MNOTIFY_API_URL + '?key=' + MNOTIFY_API_KEY,
                    json=payload,
                    headers=headers,
                    verify=True  # Enforces certificate validation using system CA store
                )

                # Append JSON Response to list
                response_list.append(response.text)

                # Response messages                
                response_message = f"PHONE NUMBER - {phone_number} | RESPONSE CODE - {response.status_code}"
                msg_logger.log('INFO', response_message)

            except AttributeError as attr_err:
                print("Missing data in row:", attr_err)
            except requests.exceptions.SSLError as ssl_err:
                print("SSL error:", ssl_err)
            except requests.exceptions.RequestException as req_err:
                print("Error sending SMS:", req_err)

        return response_list