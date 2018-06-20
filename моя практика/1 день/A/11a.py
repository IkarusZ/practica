import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input("B сантиметрах: "))

b = a * 2.54
c = 0
while b > 0:
    b -= 12
    c += 1
print('Ваш ріст: {0} футів {1} дюймів'.format(c, b))
