import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input("Введіть тиск: "))
b = float(input("Об'єм: "))
c = float(input("Температура (Цельсій): "))
R = 8.314
b3 = b/1000
g = c + 273.15
n = (a*b3)/(R*g)
print("Молярна маса газу:{:.2f}".format(n))
