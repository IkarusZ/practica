import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input("Довжина: "))
b = float(input("Ширина: "))
c = a*b
print ("Проща поля в арах: ", c / 100)
print ("Площа поля в гектарах:", c / 10000)
