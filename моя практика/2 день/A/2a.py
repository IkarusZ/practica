import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

b = []
while True:
    a = int(input('Введіть ціле число: '))
    if a == 0:
        break
    else:
        b.append(a)
b.sort()
for i in range(len(b)):
    print(b[i])
