# services/mnotify.py
import pandas as pd
import asyncio

# Import Operations
from operations.mnotify import MNOTIFYOperations

# Import Services
from services.etl import ETLService

# Import Configurations
from config import TABLE_NAME

# Instantiate Services
etl_service = ETLService()


class MNOTIFYService:

    def __init__(self):
        # Invoke MNOTIFYOperations class
        self.sender = MNOTIFYOperations()
    
    def sms_api_service(self):
        responses = asyncio.run(self.sender.process_all())

        if responses:
            dfs = pd.DataFrame({
                "Response": responses,
                "API": "mnotify"
            })

            # Check first N records
            # print(dfs.head(5))
            
            # Load data frame to MSSQL database
            etl_service.load(dfs, TABLE_NAME)

            total_records = len(dfs)
            message = f"SMS successfully sent, total records: {total_records:,}"
            print(message)