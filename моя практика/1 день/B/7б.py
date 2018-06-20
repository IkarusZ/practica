import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

print("""
1 - Будинок
2 - Квартира
3 - Гуртожиток
    """)
home = int(input('Введіть місце проживання: '))
time = int(input('Введіть скільки годин ви приблизно знаходитесь дома: '))
print('                                           ')
if home == 3:
    if time <= 6:
        print("Тобі підійде: Мурашник\n")
    elif time == 6:
        print("Тобі підійде: Мурашник або рибки\n")
    elif time >= 6:
        print("Тобі підійдуть: Рибки\n")
elif  home == 2:
    if time <= 10:
        print("Тобі підійде: Хом'як\n")
    elif time == 10:
        print("Тобі підійде: Хом'як або Кішкa\n")
    elif time >= 10:
        print("Тобі підійде: Кішка\n")
elif home == 1:
    if time <= 10:
        print("Тобі підійде: Змія\n")	
    elif time >= 10 and time <= 17:
        print("Тобі підійде: Собака\n")
    elif time >= 18:
        print("Тобі підійде: В’єтнамське порося\n")
else:
    print("Краще вам не заводити домашніх улюбленців.\n")
