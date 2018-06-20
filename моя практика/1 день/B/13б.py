from math import radians, acos, sin, cos, sqrt
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

lviv1 = radians(49)
lviv2 = radians(24)
odesa1 = radians(46)
odesa2 = radians(30)
harkiv1 = radians(50)
harkiv2 = radians(36)
a = 6371.01 * acos(sin(lviv1) * sin(lviv2) + cos(lviv1) * cos(lviv2) * cos(odesa1-odesa2))
b = 6371.01 * acos(sin(odesa1) * sin(odesa2) + cos(odesa1) * cos(odesa2) * cos(harkiv1-harkiv2))
c = 6371.01 * acos(sin(harkiv1) * sin(harkiv2) + cos(harkiv1) * cos(harkiv2) * cos(lviv1-lviv2))
p = (1/2)*(a + b + c)
S = sqrt(p * (p - a) * (p - b) * (p - c))
print('Площа: {} км^2'.format(S))
