import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

path = input('Введіть номерний знак: ')
old_letters = path[0:3] # Перші 3 букви   (old)
old_numbers = path[3:7] # Останні 3 цифри (old)
new_numbers = path[0:4] # Перші 4 цифри   (new)
new_letters = path[4:7] # Останні 3 букви (new)
old_x = old_letters.isupper() # Перевірка на правильність перших 3 букв   (old)
old_y = old_numbers.isdigit() # Перевірка на правильність останніх 3 цифр (old)
new_x = new_numbers.isdigit() # Перевірка 4 букв
new_y = new_letters.isupper() # Перевірка 3 цифр

if old_x == True and old_y == True:
	print('Цей номерний знак - старий')
elif new_x == True and new_y == True:
	print('Цей номерний знак - новий')
else:
	print('Неправильно введено номер, спробуйте по шаблону (ABC123 або 1234ABC)')
