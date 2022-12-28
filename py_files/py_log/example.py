##demo.py and examply.py are inter-related
##to show-case/demo is for creating .log file for different .py file by using logger
from demo import add_function
import logging

##using getlogger to create seperate log files
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO) ##set logging level

## formatter is to set logs format
log_format=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

## fileHandler is user to create a file
log_file=logging.FileHandler("example.log")

log_file.setFormatter(log_format)
logger.addHandler(log_file)

add_function(4,5)

logger.info("code executed successfully")