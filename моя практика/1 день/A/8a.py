import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

number = str(input('Введіть чотирьохзначне число: '))
number0 = int(number[0])
number1 = int(number[1])
number2 = int(number[2])
number3 = int(number[3])
print('Сума цифр:')
print(number0 + number1 + number2 + number3)
