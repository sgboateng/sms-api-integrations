# operations/shared.py
# Import Libraries
import pandas as pd

# Import Warnings
import warnings
warnings.filterwarnings("ignore")


class SHAREDOperations():    

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