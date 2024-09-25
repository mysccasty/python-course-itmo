#task5
from datetime import datetime
from math import floor
days_in_year = 365.25
days_in_month = 30

day = int(input("Введите день вашего рождения: "))
month = int(input("Введите месяц вашего рождения: "))
year = int(input("Введите год вашего рождения: "))
date = datetime.today()
if month in [1, 2, 3]:
    quarter = 1
elif month in [4, 5, 6]:
    quarter = 2
elif month in [7, 8, 9]:
    quarter = 3
else:
    quarter = 4

print(f"Вы родились в {quarter} квартале года.")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Год {year} является високосным.")
else:
    print(f"Год {year} не является високосным.")


days_passed = days_in_year * (date.year - year) + days_in_month * (date.month - month) + date.day - day
print(f"С вашего рождения прошло {floor(days_passed)} дней.")

