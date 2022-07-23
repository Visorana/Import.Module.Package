from package.Application.salary import calculate_salary
from package.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date.today())




