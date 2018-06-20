import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

max = int(input("Введіть розмір таблички: "))
for row in range(1, max + 1):
    for column in range(1, max + 1):
        print(row * column, end='\t')
    print()
