import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input ("Введіть кількість секунд: "))
d = str(a//86400)
h = str(a//3600)- int(d)*24
a -= int(h)*3600
m = a//60
s = a%60
if m < 10:
    m = '0' + str( m)
else:
    m = str(m)
if s < 10:
    s = '0'+str(s)
else:
    s = str(s)

print(d +':' + h + ':' + m + ':' + s)
