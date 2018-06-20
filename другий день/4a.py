import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

list1 = [1, 5, 4, 3, 1, 4, 2, 1, 4, 9, 0, 6, 6, 7, 6, 5, 1, 2, 0]
list2 = [[x,list1.count(x)] for x in set(list1)]
list3 = []
for i in range(len(list2)):
    if list2[i][1] >= 1 and list2[i][1] <= 5:
        list3.append(list2[i][0])
list3 = list(set(list3))
print(list3)
        
