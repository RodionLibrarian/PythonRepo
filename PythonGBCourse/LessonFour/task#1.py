from sys import argv


def salary_calc(time_f, salary_f, bonus_f):
    result_f = time_f * salary_f + bonus_f
    return result_f


script_name, time, salary, bonus = argv

try:
    time = float(time)
    salary = float(salary)
    bonus = float(bonus)
    result = salary_calc(time, salary, bonus)
    print(f'Salary is {result}')
except ValueError:
    print('Please enter integer variables!')
