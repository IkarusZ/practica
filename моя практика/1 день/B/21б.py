import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = input('Введіть буквенну оцінку(від A+ до F): ')
if a == 'A+' :
	print('Оцінка більше 4 балів')
elif a == 'A' :
	print('Ваша оцінка становить: 4')
elif a == 'A-' :
	print('Ваша оцінка становить: 3.7')
elif a == 'B+' :
	print('Ваша оцінка становить: 3.3')
elif a == 'B' :
	print('Ваша оцінка становить: 3.0')
elif a == 'B-' :
	print('Ваша оцінка становить: 2.7')
elif a == 'C+' :
	print('Ваша оцінка становить: 2.3')
elif a == 'C' :
	print('Ваша оцінка становить: 2.0')
elif a == 'C-' :
	print('Ваша оцінка становить: 1.7')
elif a == 'D+' :
	print('Ваша оцінка становить: 1.3')
elif a == 'D' :
	print('Ваша оцінка становить: 1.0')
elif a == 'F' :
	print('Ваша оцінка становить: 0')
else:
	print('Помилка, введіть буквенну оцінку від A+ до F')
