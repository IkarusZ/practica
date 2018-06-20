import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

phonebook = [['Пожежна безпека', '101'],
             ['Поліція', '102'],
             ['Швидка допомога', '103']]
print('''
[1] - Додати контакт
[2] - Видалити контакт
[3] - Редагувати контакт
[4] - Вивести список усіх контактів
[5] - Вийти з додатку
''')
while True:
    inp = input('Введіть номер опції: ')
    if inp == '':
        break
    else:
        inp = int(inp)
        if inp == 1:
            b = []
            name = input("Введіть ім'я: ")
            b.append(name)
            number = input('Введіть номер: ')
            b.append(number)
            phonebook.append(list(b))
            b.clear()
            print('Контакт додано!')
        elif inp == 2:
            print('Введіть порядковий номер контакту, який ви хочете видалити (від 0 до {}):'.format(len(phonebook)-1))
            a = int(input())
            phonebook.remove(phonebook[a])
            print('Номер видалено!')
        elif inp == 3:
            print('Введіть порядковий номер контакту, який ви хочете редагувати (від 0 до {}):'.format(len(phonebook)-1))
            a = int(input())
            phonebook[a][0] = input("Введіть ім'я: ")
            phonebook[a][1] = input('Введіть номер: ')
            print('Контакт відредаговано!')
        elif inp == 4:
            for i in range(0, len(phonebook)):
                print("Ім'я: {0}, номер: {1}".format(phonebook[i][0], phonebook[i][1]))
        elif inp == 5:
            break
        else:
            print('Некоректне значення')
