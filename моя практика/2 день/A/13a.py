import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

k = []
l = ['s', 'h', 'd', 'c']
s = ['J', 'Q', 'K', 'A']
for i in range(len(l)):
    for a in range(2, 11):
        b = str(a) + str(l[i])
        k.append(b)
    for c in range(len(s)):
        b = str(s[c]) + str(l[i])
        k.append(b)
print(k)
