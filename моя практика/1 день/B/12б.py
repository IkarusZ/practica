from math import radians, acos, sin, cos
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

t1 = radians(float(input('t1: ')))
g1 = radians(float(input('g1: ')))
t2 = radians(float(input('t2: ')))
g2 = radians(float(input('g2: ')))
s = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
print('Відстань: {0} км'.format(s))
