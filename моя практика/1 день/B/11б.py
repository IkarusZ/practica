import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

b = []
while True:
    a = input('Вік відвідувача: ')
    if a != '':
        a = int(a)
    else:
        break
    if a >= 0 and a < 3:
        c = 0
        b.append(c)
    elif a >= 3 and a <= 12:
        c = 16
        b.append(c)
    elif a > 60:
        c = 18
        b.append(c)
    elif a > 12 and a <= 60:
        c = 25
        b.append(c)
    else:
        print('Помилка')
if len(b) > 10:
    d = sum(b) - (sum(b) * 0.1)
else:
    d = sum(b)
d = float(d)
print('Загальна вартість: {0:.2f}'.format(d))
