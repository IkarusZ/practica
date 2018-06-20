import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input('Кількість грошей: '))
b = float(a + (a * float(0.14)))
c = float(b + (b * float(0.14)))
d = float(c + (c * float(0.14)))

print('Сума на рахунку через 1 рік: {0:>.2f}'.format(b))
print('Сума на рахунку через 2 роки: {0:>.2f}'.format(c))
print('Сума на рахунку через 3 роки: {0:>.2f}'.format(d))
