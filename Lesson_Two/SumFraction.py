"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

"""


def userInput():  # Ввод
	userEnter = input("Input the number: ")
	if (len(userEnter) >= 3):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def sumFraction(a, b):              # Метод сложения дробей
	aNumerator = int(a[len(a) - 3])
	bNumerator = int(b[len(b) - 3])
	aDenominator = int(a[len(a) - 1])
	bDenominator = int(b[len(b) - 1])
	c = f'{aNumerator * bDenominator + bNumerator * aDenominator}/{aDenominator * bDenominator}'
	return c


def multiplyFractions(a, b):        # Метод умножения дробей
	aNumerator = int(a[len(a) - 3])
	bNumerator = int(b[len(b) - 3])
	aDenominator = int(a[len(a) - 1])
	bDenominator = int(b[len(b) - 1])
	c = f'{aNumerator * bNumerator}/{aDenominator * bDenominator}'
	return c


def chooseAction(a, b):             # Выбор действия
	choice = input("Choose action with fractions:\n"
	               "1. Summ\n"
	               "2. Multiply\n")

	match (choice):
		case "1":
			return sumFraction(a, b)
		case "2":
			return multiplyFractions(a, b)


def mainMethod():                   # Главный метод
	a = userInput()
	b = userInput()
	c = chooseAction(a, b)
	print(f'Your answer is: {c}')


mainMethod()
