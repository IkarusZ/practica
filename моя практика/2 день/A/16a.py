import datetime
from random import randrange

#Прокопчук Б.Ю.!!!!
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

def sattoloCycle(items):
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        aa = k.pop(i)
        bb = k.pop(j)
        k.insert(j, aa)
        k.insert(i, bb)
    return
#Створення колоди
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
#Сортування колоди
sattoloCycle(list(k))

pq = int(input('К-сть гравців: '))
cq = int(input('К-сть карт на гравця: '))
playerlist = []
cardlist = []
cardlistt = []
for i in range(pq):
    playerlist.append('Гравець {}'.format(i))
if len(k) < (cq * pq):
    print('Error')
else:
    for kkk in range(len(playerlist)):
        for kkkk in range(cq):
            k.pop(kkkk)
            cardlistt.append(k[kkkk])
        cardlist.append(list(cardlistt))
        cardlistt.clear()
    for i in range(len(playerlist)):
        print('{0}: {1}'.format(playerlist[i], cardlist[i]))
