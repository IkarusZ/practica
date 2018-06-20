import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input('Спожита вода в кубометрах: '))
if a >= 0 and a <= 30:
    b = a * 9.86
elif a > 30 and a <= 50:
    c = a - 30
    b = (c * 11.22) + (30 * 9.86)
elif a > 50 and a <= 60:
    c = a - 30 - 50
    b = (c * 13.06) + (30 * 9.86) + (50 * 11.22)
elif a > 60:
    c = a - 30 - 50 - 10
    b = (c * 17.89) + (30 * 9.86) + (50 * 11.22) + (10 * 13.06)
else:
    print('Error')
b += 20
print('Рахунок: {0} грн.'.format(b))
