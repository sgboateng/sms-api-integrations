# services/mnotify.py
# Import Libraries
import pandas as pd
import json

# Import Operations
from operations.mnotify import MNOTIFYOperations

# Import Services
from services.etl import ETLService

# Import Utils
from utils.logger import Logger

# Import Configuations
from config import TABLE_NAME

# Instantiate Operations
mnotify_ops = MNOTIFYOperations()

# Instantiate Services
etl_service = ETLService()

# Instantiate Utils
msg_logger = Logger()


class MNOTIFYService():

    # Mnotify API service
    def sms_api_service(self) -> None:

        # Extract Soccer scores
        response_list = mnotify_ops.sms_api()

        # Check if List has records
        if len(response_list) > 0:

            # Check first N records
            print(response_list[:2])

            # Create the DataFrame directly from the Python object
            # dfs = pd.DataFrame(json.loads(response_list))

            # Create DataFrame with one column "Response"
            dfs = pd.DataFrame(response_list, columns=["Response"])

            # Add column to dataframe
            dfs['API'] = 'mnotify'

            # Check first N records
            print(dfs.head(5))

            # Load data to MSSQL database
            etl_service.load(dfs, TABLE_NAME)

            message = f"SMS successfully sent, total records: {len(dfs):,}"
            print()
            print(message)