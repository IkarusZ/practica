import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input('Число a: '))
b = int(input('Число b: '))
print('Сума: ' + str(a + b))
print('Різниця: ' + str(b - a))
print('Добуток: ' + str(b * a))
print('Частка: ' + str(a / b))
print('Остача: ' + str(a % b))
print('log10a: ' + str(math.log10(a)))
print('a^b: ' + str(a ** b))
      
