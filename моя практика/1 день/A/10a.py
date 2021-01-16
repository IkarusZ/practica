import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула')

a = int(input("Скільки штучок?"))
b = int(input("Скільки штукенцій?"))
x1 = a * 0.075
x2 = b * 0.112
x3 = x1 + x2 
print("Загальна маса замовлення: ", x3,"кг")
