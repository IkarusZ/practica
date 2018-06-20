import re
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = input('Date: ')
a = re.split(r'-', a)
year = int(a[0])
month = int(a[1])
day = int(a[2])

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    if month == 2:
        if day == 28:
            day = 29
        elif day == 29:
            day = 1
            month += 1
        elif day > 29:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day += 1
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day == 31:
            day = 1
            month += 1
        elif day > 31:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day += 1
    elif month == 4 or month == 6  or month == 9 or month == 11:
        if day == 30:
            day = 1
            month += 1
        elif day > 30:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day +=1
    elif month == 12 and day == 31:
        year += 1
        day = 1
        month = 1
    else:
        day += 1
else:
    if month == 2:
        if day == 28:
            day = 1
            month += 1
        elif day == 29:
            print('Рік не є високосним. Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        elif day > 29:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day += 1
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        if day == 31:
            day = 1
            month += 1
        elif day > 31:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day += 1
    elif month == 4 or month == 6  or month == 9 or month == 11:
        if day == 30:
            day = 1
            month += 1
        elif day > 30:
            print('Дата нижче виведеться, бо мені лінь створювати помилку, але вона не я коректною. Хе.')
        else:
            day +=1
    elif month == 12 and day == 31:
        year += 1
        day = 1
        month = 1
    else:
        day += 1
if month >= 1 and month <= 9:
    if day >= 1 and day <= 9:
        print(str(year) + '-' + '0' + str(month) + '-' + '0' + str(day))
    else:
        print(str(year) + '-' + '0' + str(month) + '-' + str(day))
else:
    print(str(year) + '-' + str(month) + '-' + str(day))
