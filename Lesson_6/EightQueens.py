"""
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
  Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
  на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
  число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль.
  Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
  Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

"""
import random

queenList = []


def fillRandomCoordinates(board):
	counter = 1

	while (counter < 9):
		x = random.randint(0, 7)
		y = random.randint(0, 7)
		board[x][y] = f' Q{counter} '
		queenList.append([x, y])
		counter += 1


def fillManualyCoordinates(board):
	counter = 1
	while (counter < 9):
		userEnter = input("Введите координаты от 1 до 8 через пробел: \n").split(" ")
		i = int(userEnter[0])
		j = int(userEnter[1])
		if (0 < i < 9 and 0 < j < 9):
			board[i - 1][j - 1] = f' Q{counter} '
			queenList.append([i - 1, j - 1])
		else:
			print("Вы ввели неверные координаты. \n"
			      "В связи с этим программа самостоятельно заполнила координаты случайным образом")
			x = random.randint(0, 7)
			y = random.randint(0, 7)
			board[x][y] = f' Q{counter} '
			queenList.append([x, y])
		counter += 1


def createBoard():
	board = [["  . " for _ in range(8)] for _ in range(8)]

	return board


def showBoard(board):
	print("       *** Ваша доска *** ")
	for row in board:
		print("".join(row))


def chooseMenu(board):
	userEnter = int(input('Выберите пункт меню: \n'
	                      '1. Заполнить доску случайно \n'
	                      '2. Заполнить доску вручную \n'))
	match (userEnter):
		case 1:
			fillRandomCoordinates(board)
		case 2:
			fillManualyCoordinates(board)
		case _:
			print("incorrect")
			chooseMenu(board)


def checkPlace(board):
	counter = 0
	for i in range(0, len(queenList)):
		for j in range(i + 1, len(queenList)):
			if (queenList[i][0] == queenList[j][0] or queenList[i][1] == queenList[j][1]):
				print("False")
			else:
				print("True")


def mainMethod():
	board = createBoard()
	chooseMenu(board)
	showBoard(board)
	print()
	print(queenList)
	checkPlace(board)


mainMethod()
