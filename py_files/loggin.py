import logging

logging.basicConfig(level=logging.INFO, filename="logFile.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

x = 2

##logging should be in this format only
logging.debug('Starting')
logging.info(f"the value of x is {x}")
logging.warning('warn')
logging.error('error')
logging.critical('critical')

print("\n << eg 2 logging.error >> \n")
#================================================================
# try:
#     1/0
# except Exception as e:
#     logging.error(e,exc_info=True)
    
print("\n << eg 3 logging.error >> \n")
#================================================================

try:
    1/0
except Exception as e:
    logging.exception(f"this is an exception {e}")