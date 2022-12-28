##ref: https://www.youtube.com/watch?v=gsa1oFn9n0M
import logging

##using getlogger to create seperate log files
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO) ##set logging level

## formatter is to set logs format
log_format=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

## fileHandler is user to create a file
log_file=logging.FileHandler("demo.log")

log_file.setFormatter(log_format)
logger.addHandler(log_file)

## logging configuration
# logging.basicConfig(level=logging.INFO, filemode="w",filename="demo.log",
#                     format="%(asctime)s - %(levelname)s - %(message)s")

## demo function
def demo_functions():
    logger.info("this is a demo function")

demo_functions()

## add function
def add_function(a,b):
    sum=a+b
    print(sum)
    logger.info(sum)
    