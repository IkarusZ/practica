import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input('Кількість використаних хвилин: '))
b = int(input('Кількість використаних повідомлень: '))
tar = float(15)

if a >= 0 and a <= 200:
    tar += 0
elif a > 200:
    extram = (a - 200) * 0.17
    tar += extram
else:
    print('')

if b >= 0 and a <= 50:
    tar += 0
elif b > 50:
    extras = (b - 50) * 0.15
    tar += extras
else:
    print('')
c = tar + 0.44 + (tar * 0.05)
print('Базова плата за користування: {0:>.2f}'.format(tar))
print('Загалний рахунок для користувача: {0:>.2f}'.format(c))
