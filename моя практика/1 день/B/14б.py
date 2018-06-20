import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = int(input('Введіть рік: '))
while a < 2000 or a > 2011:
    if a >= 2000 and a <= 2011:
        break
    elif a < 2000:
        a += 12
    elif a > 2011:
        a -= 12
    elif a < 0:
        print('Введіть рік нашої ери')
        break
    else:
        break
if a == 2000:
    print('Dragon')
elif a == 2001:
    print('Snake')
elif a == 2002:
    print('Horse')
elif a == 2003:
    print('Sheep')
elif a == 2004:
    print('Monkey')
elif a == 2005:
    print('Rooster')
elif a == 2006:
    print('Dog')
elif a == 2007:
    print('Pig')
elif a == 2008:
    print('Rat')
elif a == 2009:
    print('Ox')
elif a == 2010:
    print('Tiger')
elif a == 2011:
    print('Hare')
else:
    print('Error')
        
