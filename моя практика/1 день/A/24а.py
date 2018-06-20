import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

s = float(input('Довжина: '))
n = float(input('К-сть сторін: '))
print('Площа: ' + str((n * s ** 2)/(4 * math.tan(math.pi/n))))
