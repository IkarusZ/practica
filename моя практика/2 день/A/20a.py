import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

b = []
d = []
e = []
while True:
    a = input('Введіть число: ')
    if a != '':
        a = float(a)
        b.append(a)
    else:
        break
c = sum(b) / len(b)
for i in range(len(b)):
    if b[i] < c:
        d.append(b[i])
    elif b[i] >= c:
        e.append(b[i])
    else:
        print('')
print('Список чисел, які менші за середнє значення: {}'.format(d))
print('Список чисел, які більші або рівні середньому значенню: {}'.format(e))
