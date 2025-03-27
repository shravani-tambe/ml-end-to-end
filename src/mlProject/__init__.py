import os 
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

'''%(asctime)s: Timestamp of when the log entry was created
%(levelname)s: Logging level (e.g., INFO, DEBUG, ERROR)
%(module)s: Name of the module where the logging call was made'''

log_dir = "logs" 

log_filpath = os.path.join(log_dir, "running_log.log")

os.makedirs(log_dir, exist_ok=True)

'''creates a directory named "logs" if it doesn't exist
defines the full path for the log file as "logs/running_log.log"
exist_ok=True prevents errors if the directory already exists'''

logging.basicConfig(
    level = logging.INFO, 
    format = logging_str, 
    handlers = [
        logging.FileHandler(log_filpath), 
        logging.StreamHandler(sys.stdout)
    ]
)

'''level=logging.INFO: Sets minimum severity level to INFO (will log INFO, WARNING, ERROR, CRITICAL)
FileHandler: Writes logs to the file specified (running_log.log)
StreamHandler(sys.stdout): Outputs logs to console/terminal'''

logger = logging.getLogger("mlProjectLogger")