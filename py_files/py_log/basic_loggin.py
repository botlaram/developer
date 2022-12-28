import logging

logging.basicConfig(level=logging.INFO, filename="basic_loggin.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)s - %(message)s")  ##funcname display the actual fnction name

x = 2

##logging should be in this format only
logging.debug('Starting')
logging.info(f"the value of x is {x}")
logging.warning('warn')
logging.error('error')
logging.critical('critical')

print("\n << eg 2 logging.error >> \n")
#================================================================
##using error as exception

def logs():
    try:
        1/0
    except Exception as e:
        logging.error(e,exc_info=True)
logs()
  
print("\n << eg 3 logging.error >> \n")
#================================================================
##usin exception as exception by replacing error

try:
    1/0
except Exception as e:
    logging.exception(f"this is an exception {e}")