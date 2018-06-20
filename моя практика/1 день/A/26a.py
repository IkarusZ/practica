import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = input('Сторона 1: ')
b = input('Сторона 2: ')
c = input('Сторона 3: ')

if a == b and b == c:
    print('Трикутник рівносторонній')
elif a == b or a == c or b == c:
    print('Трикутник рівнобедрений')
else:
    print('Трикутник різносторонній')
