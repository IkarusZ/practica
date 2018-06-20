import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

while True:
    a = input('IMEI: ')
    a = list(a)
    if len(a) != 14:
        continue
    else:
        break
b = a[0] + (a[1] * 2) + a[2] + (a[3] * 2) + a[4] + (a[5] * 2) + a[6] + (a[7] * 2) + a[8] + (a[9] * 2) + a[10] + (a[11] * 2) + a[12] + (a[13] * 2)
b = list(b)
c = int(b[1])
if c == 0:
    l = 0
else:
    l = 10 - c
if l == 6:
    print('IMEI відповідає Луна 6')
else:
    print('IMEI не відповідає Луна 6')
