import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

listt = [3, 5, 6, 1, 9, 5, 2, 7, 3, 4, 10, 9]
print(listt)
n = []
for i in listt:
    if i not in n:
        n.append(i)
listt.clear()
listt = n.copy()
n.clear()
print(listt)
list2 = listt.copy()
print(list2)
list2.remove(list2[0])
list2.remove(list2[1])
list2.remove(list2[1])
print(list2)
