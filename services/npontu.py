# services/npontu.py
import pandas as pd
import asyncio

# Import Operations
from operations.npontu import NPONTUOperations

# Import Services
from services.etl import ETLService

# Import Configurations
from config import TABLE_NAME

# Instantiate Services
etl_service = ETLService()


class NPONTUService:

    def __init__(self):
        # Invoke NPONTUOperations class
        self.sender = NPONTUOperations()
    
    def sms_api_service(self):
        responses = asyncio.run(self.sender.process_all())

        if responses:
            dfs = pd.DataFrame({
                "Response": responses,
                "API": "npontu"
            })

            # Check first N records
            # print(dfs.head(5))
            
            # Load data frame to MSSQL database
            etl_service.load(dfs, TABLE_NAME)

            total_records = len(dfs)
            message = f"SMS successfully sent, total records: {total_records:,}"
            print(message)