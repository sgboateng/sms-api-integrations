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

# Mnotify API Credentials
MNOTIFY_API_URL = os.getenv("MNOTIFY_API_URL")
MNOTIFY_API_KEY = os.getenv("MNOTIFY_API_KEY")

# Npontu API Credentials
NPONTU_USER_NAME = os.getenv("NPONTU_USER_NAME")
NPONTU_PASSSWORD = os.getenv("NPONTU_PASSSWORD")
NPONTU_API_URL = os.getenv("NPONTU_API_URL")

# Batch size
BATCH_SIZE = int(os.getenv("BATCH_SIZE", 10000))

# Concurrency limit
CONCURRENCY_LIMIT=int(os.getenv("CONCURRENCY_LIMIT", 100))

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