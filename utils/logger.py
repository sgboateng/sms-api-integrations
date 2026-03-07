# utils/logger.py
# Import libraries
import logging

import warnings
warnings.filterwarnings('ignore')

# Import Configuations
from config import LOG_FILE


class Logger:

    # Logging Method
    def log(self, level: str, message: str) -> None:
        
		# Configurations
        date_format = '%Y-%m-%d %H:%M:%S'        
        log_format = '%(asctime)s %(levelname)s: %(message)s'
        logger = logging.getLogger("Custom Logger")
        
        # Set logging level
        logger.setLevel(logging.INFO)
        
        # FileHandler configuration
        file_handler = logging.FileHandler(LOG_FILE, mode='a')
        formatter = logging.Formatter(log_format, date_format)
        file_handler.setFormatter(formatter)
        
        # Clear all file handlers
        if (logger.hasHandlers()):
            logger.handlers.clear()
        
        # Add new file handler
        logger.addHandler(file_handler)
        
        # Check level before logging
        if level == 'INFO':
            logger.info(message)
        else:
            logger.error(message)