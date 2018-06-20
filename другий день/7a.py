import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

list1 = []
while True:
    a = input('Введіть слово: ')
    if a == '':
        break
    else:
        list1.append(a)

list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
