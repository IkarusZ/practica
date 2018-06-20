import re
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

while True:
    try:
        numlet = input('Позиція: ')
        list1 = re.findall(r'\D+', numlet)
        list2 = re.findall(r'\d+', numlet)
        let = ''.join(list1)
        num = ''.join(list2)
        num = int(num)
    except ValueError:
        print('Некоректне значення. Спробуйте ще раз.')
        continue
    if num < 1 and num > 8:
        print('Некоректне значення. Спробуйте ще раз.')
        continue
    elif let == "a" or let == "b" or let == "c" or let == "d" or let == "e" or let == "f" or let == "g" or let == "h":
        break
    else:
        print('Некоректне значення. Спробуйте ще раз.')
        continue
if num % 2 == 0:
    if let == "a" or let == "c" or let == "e" or let == "g":
        print('Біла')
    elif let == "b" or let == "d" or let == "f" or let == "h":
        print('Чорна')
else:
    if let == "a" or let == "c" or let == "e" or let == "g":
        print('Чорна')
    elif let == "b" or let == "d" or let == "f" or let == "h":
        print('Біла')
