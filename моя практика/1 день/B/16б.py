import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

t = float(input('Введіть температуру повітря: '))
v = float(input('Введіть швидкість вітру: '))

check = 0
check_t = 0
check_v = 0

if t >= 10:
    check = 1
    check_t = 1
else:
    check = 0
if v <= 4.8:
    check = 1
    check_v = 1
else:
    check = 0

while check == 0:
    v = v**0.16
    wci = 13.12 + (0.6215*t) + (11.37*v) + (0.3965*t*v)
    print (wci)
    check = 1
else:
    if check_t == 1:
        print ('Висока температура повітря')
    if check_v == 1:
        print ('Мала швидкість вітру')
