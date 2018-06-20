import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

M = int(0)
p = float(1038)
c = 3700
K = float(5.4 * (10 ** 5))
Tw = float(100)
while M == 0:
    a = int(input('Яйце велике чи маленьке? (1/2): '))
    if a == 1:
        M = 0.067
    elif a == 2:
        M = 0.047
    else:
        print('Введіть значення 1 або 2')
Ty = float(input('Введіть температуру жовтка: '))
T0 = 0
while T0 == 0:
    b = int(input('Яйце з холодильника чи кімнатної температури? (1/2): '))
    if b == 1:
        T0 = float(4)
    elif b == 2:
        T0 = float(20)
    else:
        print('Введіть значення 1 або 2')

t = ((M ** (2/3)) * c * (p ** (1/3)))/(K * (math.pi ** 2) * (((4 * math.pi)/3) ** (2/3))) * math.log(float(0.76) * (((T0 + 273.15) - (Tw + 273.15))/((Ty + 273.15) - (Tw + 273.15))))
print('Час, коли центр жовтка досягне температури Ty: ' + str(t))
