import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input('Decibel level (dB): '))
if a == 40:
    print('Quiet room')
elif a == 70:
    print ('Alarm clock')
elif a == 106:
    print('Gas lawnmower')
elif a == 130:
    print('Jackhammer')
elif a >= 0 a < 40:
    print('Less than Quiet room')
elif a > 40 and a < 70:
    print('Quiet room <=> Alarm clock')
elif a > 70 and a < 106:
    print('Alarm clock <=> Gas lawnmower')
elif a > 106 and a < 130:
    print('Gas lawnmower <=> Jackhammer')
elif a > 130:
    print('More than Jackhammer')
else:
    print('Error')
