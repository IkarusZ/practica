import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

a = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

b = dict(sorted(a.items(), key=lambda value: value[1]))
print(b)
c = dict(sorted(a.items(), key=lambda value: value[:1]))
print(c)
d = dict(list(b.items()) + list(c.items()))
print(d)
