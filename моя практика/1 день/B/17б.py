import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Пікула. Погорілий')

time = int(input("Введіть рік:"))

if time % 400 == 0 :
	print("Данний рік високосний")
elif time % 100 == 0 :
	print("Данний рік  не високосний") 
elif time % 4 == 0 :
	print("Данний рік високосний")
else :
	print("Данний рік  не високосний")





