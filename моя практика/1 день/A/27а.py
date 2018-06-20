import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')


a = input('Чи говорить папуга (ТАК/НІ)? ')
b = float(input('Котра година (ГГ.ХХ): '))
b = int(b)

if a == 'ТАК':
    if b >= 22 and b <=23 or b >= 0 and b <= 8:
        print('Накрити рядниною.')
    else:
        print('Не чіпати.')
else:
    print('Не чіпати.')
