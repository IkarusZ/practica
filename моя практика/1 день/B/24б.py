import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = float(input('hZ: '))
if a < (3 * (10 ** 9)):
    print('Radio waves')
elif a >= (3 * (10 ** 9)) and a < (3 * (10 ** 12)):
    print('Microwaves')
elif a >= (3 * (10 ** 12)) and a < (4.3 * (10 ** 14)):
    print('Infrared light')
elif a >= (4.3 * (10 ** 14)) and a < (7.5 * (10 ** 14)):
    print('Visible light')
elif a >= (7.5 * (10 ** 14)) and a < (3 * (10 ** 17)):
    print('Ultraviolet light')
elif a >= (3 * (10 ** 17)) and a < (3 * (10 ** 19)):
    print('X-rays')
elif a > (3 * (10 ** 19)):
    print('Gamma rays')
else:
    print('Error')
