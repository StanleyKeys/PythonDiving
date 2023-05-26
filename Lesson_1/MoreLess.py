"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
import random


def userInput():  # Ввод
	userEnter = input("Input the number: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def playGame(num, tries):
	if (tries == 0):
		print("Sorry. But you haven't got any tries. \nGAME OVER")
	else:
		print(f"\nYou have {tries} tries\n")
		a = int(userInput())
		if (a == num):
			print(f"Yes! Thats it! \nMy number is {num} \nCongratulations!")
		elif (a > num):
			print("Your number is bigger than mine")
			tries -= 1
			playGame(num, tries)
		elif (a < num):
			print("Your number is less than mine")
			tries -= 1
			playGame(num, tries)


def mainMethod():
	print("Hello! Im J.A.R.V.I.S! \nTry to beat me!")
	num = random.randint(0, 1000)
	tries = 10
	print(num)
	playGame(num, tries)

mainMethod()