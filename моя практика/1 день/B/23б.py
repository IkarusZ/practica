import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

n = int(input('Число 1: '))
m = int(input('Число 2: '))
a = n - m
if a > 0:
    d = m
elif a < 0:
    d = n
elif a == 0:
    d = m
else:
    print('')
while n % d != 0 or m % d != 0:
    d -= 1
print('НСД: ' + str(d))
