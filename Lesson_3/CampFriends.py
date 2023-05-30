"""
Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
- Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
import random

itemList = ["Палатка", "Тент", "Топор", "Газовка", "Котелок", "Чайник", "Миска",
            "Складная пила", "Ведро", "Веревка", "Аптечка", "Аккумулятор"]

friendsDict = {}


def userInput():  # Ввод
	userEnter = input("Input the amount of Friends: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def shuffleList():  # Перемешиваем список вещей
	tempList = itemList
	random.shuffle(tempList)
	return tempList


def fillFriendsDict(friendsAmount):
	counter = 1
	limitOfItems = int(len(itemList) / 1.5)  # Присвоен лимит вещей, чтоб можно было проверять их уникальность
	while (counter <= friendsAmount):
		bag = shuffleList()
		friendsDict[f"Друг № {counter}"] = sorted(bag[0:limitOfItems])
		counter += 1


def showDict(dict):  # Красивый вывод словаря
	for element in dict:
		print(element)
		for item in dict[element]:
			print(item)
		print("- = - = - = - = - ")


def searchUnicItems(friendsAmount):  # Метод возвращает новый словарь с друзьями и НЕвзятыми вещами у каждого.
	unicItems = friendsDict.copy()
	counter = 1
	while (counter <= friendsAmount):
		tempList = unicItems[f'Друг № {counter}']
		for element in unicItems:
			if (unicItems[element] != unicItems[f'Друг № {counter}']):
				for item in unicItems[element]:
					if item in tempList:
						unicItems[element].remove(item)
		counter += 1
	return unicItems


def mainMethod():
	friendsAmount = int(userInput())
	fillFriendsDict(friendsAmount)
	# showDict(friendsDict)
	print(friendsDict)
	unicDict = searchUnicItems(friendsAmount)
	showDict(unicDict)


mainMethod()
