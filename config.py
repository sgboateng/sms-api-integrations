# config.py
# Import Libraries
import os
from dotenv import load_dotenv

# Import Warnings
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

# Excel file path
PATH = os.getenv("PATH")

# Log file
LOG_FILE = os.getenv("LOG_FILE")

# API Credentials
MNOTIFY_API_KEY = os.getenv("MNOTIFY_API_KEY")
MNOTIFY_API_URL = os.getenv("MNOTIFY_API_URL")

# Concurrent Requests
CONCURRENT_REQUESTS = int(os.getenv("CONCURRENT_REQUESTS", 20))

# Database connection details
driver = os.getenv("DB_DRIVER")
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# MSSQL connection string
connection_string = (
    f"DRIVER={{{driver}}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password}"
)

# Table names
TABLE_NAME = os.getenv("TABLE_NAME")