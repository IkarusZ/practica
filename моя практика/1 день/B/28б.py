import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

s = []
a = 2
pi = float(3)
for i in range(15):
    b = a + 1
    c = b + 1
    d = 4/(a * b * c)
    s.append(d)
    a = c
for i in range(0,14):
    pi += s[i] - s[i+1]
    print(pi)
