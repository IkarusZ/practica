import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

path = input('Введіть свій день та місяць народження: ')
x = path.split()
month = x[1]
day = int(x[0])

if month == 'Грудня' and day >= 22 and day <= 31 or month == 'Січня' and day >= 1 and day<= 19:
	print('Козерог')
elif month == 'Січня' and day >=20 and day <= 31 or month == 'Лютого' and day >=1 and day <= 18:
	print('Водолій')
elif month == 'Лютого' and day >=19 and day <= 31 or month == 'Березня' and day >=1 and day <= 20:
	print('Риби')
elif month == 'Березня' and day >=21 and day <= 31 or month == 'Квітня' and day >=1 and day <= 19:
	print('Овен')
elif month == 'Квітня' and day >=20 and day <= 31 or month == 'Травня' and day >=1 and day <= 20:
	print('Телець')
elif month == 'Травня' and day >=21 and day <= 31 or month == 'Червня' and day >=1 and day <= 20:
	print('Близнюки')
elif month == 'Червня' and day >=21 and day <= 31 or month == 'Липня' and day >=1 and day <= 22:
	print('Рак')
elif month == 'Липня' and day >=23 and day <= 31 or month == 'Серня' and day >=1 and day <= 22:
	print('Лев')
elif month == 'Серпень' and day >=23 and day <= 31 or month == 'Вересень' and day >=1 and day <= 22:
	print('Діва')
elif month == 'Вересня' and day >=23 and day <= 31 or month == 'Жовтня' and day >=1 and day <= 22:
	print('Терези')
elif month == 'Жовтня' and day >=23 and day <= 31 or month == 'Листопада' and day >=1 and day <= 21:
	print('Скорпіон')
elif month == 'Листопада' and day >=22 and day <= 31 or month == 'Грудня' and day >=1 and day <= 21:
	print('Стрілець')
