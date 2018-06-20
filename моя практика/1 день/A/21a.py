import math
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input("Ціле число: "))
s = (a*(a + 1))/2


print ("Сума: ",s)

