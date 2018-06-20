import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

b = []
def iff(a):
    if a >= 0 and a < 1:
        print('F')
    elif a >= 1 and a < 1.3:
        print('D')
    elif a >= 1.3 and a < 1.7:
        print('D+')
    elif a >= 1.7 and a < 2.0:
        print('C-')
    elif a >= 2.0 and a < 2.3:
        print('C')
    elif a >= 2.3 and a < 2.7:
        print('C+')
    elif a >= 2.7 and a < 3.0:
        print('B-')
    elif a >= 3.0 and a < 3.3:
        print('B')
    elif a >= 3.3 and a < 3.7:
        print('B+')
    elif a >= 3.7 and a < 4:
        print('A-')
    elif a == 4:
        print('A')
    elif a > 4:
        print('A+')
    else:
        print('Такого значення немає у таблиці')
while True:
    a = float(input(''))
    if a == -1:
        break
    elif a > 0:
        iff(a)
        b.append(a)
    else:
        print('Error')
s = (sum(b))/len(b)
print(s)
iff(s)
