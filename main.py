import datetime

from application.salary import calculate_salary
from application.people import get_employees

if __name__ == '__main__':
    d = datetime.date.today()
    calculate_salary(), print(d)
    get_employees(), print(d)
