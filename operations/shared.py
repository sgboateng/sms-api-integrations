# operations/shared.py
# Import Libraries
import pandas as pd

# Import Warnings
import warnings
warnings.filterwarnings("ignore")


class SHAREDOperations():    

    # Create Contact list
    def contact_list(self) -> pd.DataFrame:

        # Contacts list
        contacts = {
        'customer_name': ['Samuel Boateng', 'Kofi Gyebi', 'Nana Baffuor', 'Gafar Yahaya', 'Amin Gafar'],
        'account_number': ['******5249', '******0918', '******5493', '******2589', '******5282'],
        'phone_number': ['******2622', '******5172', '******0277', '******5277', '******8126'],
        'expiry_date': ['2026-11-19', '2026-04-01', '2026-09-21', '2026-03-14', '2026-07-25']
        }

        # Convert dictionary to Pandas dataframe
        df_contacts = pd.DataFrame(contacts)

        # Convert the 'expiry_date' column to datetime
        df_contacts['expiry_date'] = pd.to_datetime(df_contacts['expiry_date'])

        return df_contacts