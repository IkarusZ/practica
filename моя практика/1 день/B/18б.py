import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

x1 = float(input('Enter the x part of the coordinate: '))
y1 = float(input('Enter the y part of the coordinate: '))
xt = x1
yt = y1
p = 0
while True:
    x = input('Enter the x part of the coordinate (blank to quit): ')
    if x != '':
        x = float(x)
    else:
        break
    y = float(input('Enter the y part of the coordinate: '))
    d = math.sqrt(((x - xt) ** 2) + ((y - yt) ** 2))
    p += d
    xt = x
    yt = y
d = math.sqrt(((xt - x1) ** 2) + ((yt - y1) ** 2))
p += d
print('The perimeter of that polygon is ' + str(p))
