"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""

dict = {}


def userInput():
	userEnter = input("Введите 3 ключевых параметра через пробел: ").split(" ")
	if (len(userEnter) == 3):
		return userEnter
	else:
		print("Incorrect length")
		return userInput()


def createDict(*arguments, **keywords):
	for kw in keywords:
		dict[keywords[kw]] = f'{kw}'


def mainMethod():
	userEnter = userInput()
	createDict(first=userEnter[0], second=userEnter[1], third=userEnter[2])
	print(dict)


mainMethod()
