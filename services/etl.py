# services/etl.py
# Import Libraries
import pandas as pd
import os
from contextlib import contextmanager

import warnings
warnings.filterwarnings('ignore')

# Import Logger
from utils.logger import Logger

# Import References
from db.sms_api_integrations_db import db_connection

# Instantiate Logger
msg_logger = Logger()


class ETLService():

    # Context manager to safely change working directory
    @contextmanager
    def change_directory(self, path: str):

        # Get current working directory
        original_dir = os.getcwd()

        # Change working directory
        os.chdir(path)

        try:
            yield
        finally:
            os.chdir(original_dir)

    # Load data to MSSQL database
    def load(self, data_frame: pd.DataFrame, destination: str) -> None:

        try:        
            # Insert Pandas dataframe into SQL DB
            # NB: replace: drops the table before inserting new values || append: inserts new values to the existing table
            data_frame.to_sql(destination, schema='dbo', con=db_connection(), chunksize=5000, index=False, if_exists='append')

        except Exception as error:
            print(error + '\n')