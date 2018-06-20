import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = input('Введіть назву місяця: ')
if a == "Січень" or a == "Березень" or a == "Травень" or a == "Липень" or a == "Серпень" or a == "Жовтень" or a == "Грудень":
    print('У місяці 31 день')
elif a == "Квітень" or a == "Червень" or a == "Вересень" or a == "Листопад":
    print('У місяці 30 днів')
elif a =="Лютий":
    print('У місяці 28 або 29 днів')
else:
    print('Помилка')
