import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

playlist = [['Seven Devils', 'Florence + The Machine', 'Ceremonials', 5.03],
            ['Primo Victoria', 'Van Canto', 'Break the Silence', 3.44],
            ['Your Affection', 'Sapphire', 'The Velvet Lounge', 4.25],
            ['Paint It, Black', 'The Rolling Stones', 'Unknown', 3.22],
            ['Motteke! Sailor Fuku (Lucky Star)', 'AmaLee', 'Nostalgia II', 4.16]]
print('''
[1] - Додати пісню
[2] - Видалити пісню
[3] - Отримати розмір
[4] - Очистити плейлист
[5] - Вивести композиції
[6] - Вивести тривалість плейлисту
''')
while True:
    inp = input('Введіть номер опції: ')
    if inp == '':
        break
    else:
        inp = int(inp)
        if inp == 1:
            b = []
            name = input('Введіть назву пісні: ')
            b.append(name)
            artist = input('Введіть автора: ')
            b.append(artist)
            album = input('Назва альбому: ')
            b.append(album)
            duration = float(input('Тривалість: '))
            b.append(duration)
            playlist.append(list(b))
            b.clear()
            print('Пісню додано!')
        elif inp == 2:
            print('Введіть порядковий номер пісні, яку ви хочете видалити (від 0 до {}):)'.format(len(playlist)-1))
            a = int(input())
            playlist.remove(playlist[a])
            print('Пісню видалено!')
        elif inp == 3:
            print('В плейлисті {} пісні'.format(len(playlist)))
        elif inp == 4:
            playlist.clear()
            print('Плейлист очищено!')
        elif inp == 5:
            for i in range(0, len(playlist)):
                print('{1} - {0} ({2}), {3}'.format(playlist[i][0], playlist[i][1], playlist[i][2], playlist[i][3]))
        elif inp == 6:
            c = []
            for i in range(len(playlist)):
                c.append(playlist[i][3])
            print('Загальна тривалість плейлисту: {}'.format(sum(c)))
        else:
            print('Некоректне значення, спробуйте ще раз')
              
