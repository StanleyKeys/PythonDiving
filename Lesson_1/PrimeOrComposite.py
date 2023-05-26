
"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""


def userInput():                # Ввод
	userEnter = input("Input the number: ")
	if (userEnter.isdigit()):
		if (int(userEnter) <= 0 or int(userEnter) > 100000):
			print("Number must be between 1 and 100k")
			return userInput()
		return userEnter
	else:
		print("incorrect")
		return userInput()


def checkPrimeOrComposite(x):  # Проверка на Простоту
	k = 0
	for i in range(2, x // 2 + 1):
		if (x % i == 0):
			k = k + 1
	if (k <= 0):
		print(f'Your number "{x}" is Prime')
	else:
		print(f'Your number "{x}" is Composite')


def mainMethod():             # Главный метод
	x = int(userInput())
	checkPrimeOrComposite(x)


mainMethod()
