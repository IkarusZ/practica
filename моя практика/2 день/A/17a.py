import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = []
b = 2
c = 0
for i in range(1, 10000):
    while b <= i:
        if i % b == 0:
            c += i // b 
            b += 1
        else:
            b += 1
    if c == i:
        a.append(i)
    b = 2
    c = 0
print(a)
