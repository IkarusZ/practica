import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

scrabble = {'A':1,
            'E':1,
            'I':1,
            'L':1,
            'N':1,
            'O':1,
            'R':1,
            'S':1,
            'T':1,
            'U':1,
            'D':2,
            'G':2,
            'B':3,
            'C':3,
            'M':3,
            'P':3,
            'F':4,
            'H':4,
            'V':4,
            'W':4,
            'Y':4,
            'K':5,
            'J':8,
            'X':8,
            'Q':10,
            'Z':10}
while True:
    a = list(input('Введіть слово: '))
    if a == []:
        break
    else:
        b = []
        for i in range(len(a)):
            a[i] = a[i].upper()
        for i in scrabble:
            for n in range(len(a)):
                if i == a[n]:
                    b.append(scrabble.get(i))
        print(sum(b))
