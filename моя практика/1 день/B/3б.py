import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

sp1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sp = []
for i in range(len(sp1)):
    c = sp1[i] * 9/5 + 32
    sp.append(c)

for i in range(len(sp)):
    print('{0} °C       ==>       {1} ºF'.format(sp1[i], sp[i]))
