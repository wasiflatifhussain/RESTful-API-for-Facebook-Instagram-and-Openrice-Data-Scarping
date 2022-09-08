import logging
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#to be used for naming the files for each day basis
x = datetime.datetime.now()
y1 = x.strftime("%d") 
y2 = x.strftime("%b")
y3 = x.strftime("%Y")
# x.strftime("%x")


file_handler = logging.FileHandler(f"logs/employees-{y1}-{y2}-{y3}.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)