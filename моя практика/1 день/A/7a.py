import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input("Градус в Цельсіях: "))
print ("В Кельвінах: ", a + 273.15)
print ("В Фаренгейтах: ", a * 9/5 + 32.)
