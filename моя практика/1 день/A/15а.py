import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')
a = 1
b = []
while True:
    a = int(input('Введіть число: '))
    if a != 0:
        b.append(a)
    else:
        break
if b[0] == 0:
    print('Помилка!')
else:
    print('Середнє значення: ' + str(sum(b) / len(b)))
