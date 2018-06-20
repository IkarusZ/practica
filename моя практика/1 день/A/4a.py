import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

l = input("Введіть букву: ")
if l in ('a', 'e', 'i', 'o', 'u'):
        print("%s - голосна." % l)
elif l == 'y':
        print("%s - інколи голосна, інколи приголосна")
else:
        print("%s - приголосна." % l) 
