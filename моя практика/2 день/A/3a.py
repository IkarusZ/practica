import random
import itertools
import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

listt = [1, 56, 3, 7, 13, 67]
random.shuffle(listt)
print(listt)
print(list(itertools.permutations(listt)))
for i in range(8):
    listt.append(random.randint(0, 1000))
print(' ')
print(listt)
