import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input("Ведіть число контейнерів до 1л.: "))
b = int(input("Ведіть число контейнерів більше 1л.: "))
e1 = a * 0.1
e2 = b * 0.25
e3 = e1 + e2
print("Гроші за контейнери до 1л.: $",+ e1)
print("Гроші за контейнери більше 1л.: $",+ e2)
print("Разом: $",+ e3)
