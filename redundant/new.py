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


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')