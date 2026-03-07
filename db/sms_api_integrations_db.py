# db/sportsanalytics.py
# Import Libraries
import urllib
from sqlalchemy import create_engine

# Import Configuations
from config import connection_string

# Sports Analytics DB Connection
def db_connection():
    
    con = urllib.parse.quote_plus(connection_string)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={con}", fast_executemany=True)

    return engine