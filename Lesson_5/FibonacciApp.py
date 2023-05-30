"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""


def userInput():  # Ввод
	userEnter = input("Input the number: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def fib(userNumber):  # Метод вычисления порядка Фибоначчи
	fib1 = fib2 = 1
	print(fib1, fib2, end=' ')
	for i in range(2, userNumber):
		fib1, fib2 = fib2, fib1 + fib2
		print(fib2, end=' ')


def mainMethod():
	userNumber = int(userInput())
	fib(userNumber)


mainMethod()
