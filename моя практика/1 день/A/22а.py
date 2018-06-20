import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

r = float(input('Введіть радіус: '))
print('Площа круга: ' + str(math.pi * (r ** 2)))
print("Об'єм кулі: " + str(4/3 * math.pi * (r ** 3)))
