import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')
aa = input('Брати дані у м і кг чи фунтах і дюймах? (1/2)')
if aa == '1':
    a = float(input('Введіть ріст (м): '))
    b = float(input('Введіть масу (кг): '))
    print('ІМТ: ' + str(b / (a ** 2)))
else:
    a = float(input('Введіть ріст (фунти): '))
    b = float(input('Введіть масу (дюйми): '))
    print('ІМТ: ' + str(703 * b / (a ** 2)))
