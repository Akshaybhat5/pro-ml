#libraries
import os
import logging
from datetime import datetime

#log format
LOG_FILE_FORMAT = f"{datetime.now().strftime('%m_%d_%Y_%M_%H_%S')}.log"
#directory
log_file_directory = os.path.join(os.getcwd(), "log", LOG_FILE_FORMAT)
#create this directory
os.makedirs(log_file_directory, exist_ok=True)

#log file final file name
LOG_FILE_NAME = os.path.join(log_file_directory, LOG_FILE_FORMAT)

#logging information
logging.basicConfig(
    filename=LOG_FILE_NAME,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)