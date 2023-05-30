"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""
import random
from collections import OrderedDict

campItems = {
	"Палатка": 4,
	"Тент": 3,
	"Топор": 3,
	"Складная пила": 2,
	"Газовка": 4,
	"Котелок": 1,
	"Чайник": 1,
	"Миска": 1,
	"Универсальный нож": 1,
	"Разделочная доска": 1,
	"Решетка гриль": 1,
	"Ведро": 2,
	"Веревка": 3,
	"Аптечка": 5,
	"Аккумулятор": 1,
	"Телефон": 1
}


def userInput():  # Ввод
	userEnter = input("Введите вес вашего рюкзака: ")
	if (userEnter.isdigit()):
		if (int(userEnter) >= 3):
			return userEnter
		else:
			print("Ваш рюкзак не сможет ничего вместить. \nМинимальная грузоподьемность ваших вещей не менее 3кг")
			return userInput()
	else:
		print("incorrect")
		return userInput()


def getVariantsAmount():  # Ввод для количества вариантов
	userEnter = input("Сколько вариантов вы хотите увидеть?: ")
	if (userEnter.isdigit()):
		if (int(userEnter) > 0):
			return userEnter
		else:
			print("Число должно быть положительным \n")
			return userInput()
	else:
		print("incorrect")
		return userInput()


def createBagVariants(bagCapacity):  # Создание варианта
	keys = list(campItems.keys())
	random.shuffle(keys)
	randomDict = OrderedDict([(k, campItems[k]) for k in keys])  # Создаем словарь со случайными "<К, V>"
	itemList = []
	weight = bagCapacity
	for element in randomDict:
		if (randomDict[element] <= weight):
			itemList.append(element)
			weight -= randomDict[element]
	itemList.append(f'Осталось {weight} кг')
	return itemList


def addVariant(bagCapacity):  # Добавление варианта в словарь
	variantAmount = 1
	limit = int(getVariantsAmount())
	resultDict = {}
	while (variantAmount <= limit):
		itemList = createBagVariants(bagCapacity)
		resultDict[f"Вариант №{variantAmount}"] = itemList
		variantAmount += 1
	return resultDict


def showDict(dict):  # Красивый вывод словаря
	for element in dict:
		print(element)
		for item in dict[element]:
			print(item)
		print("- = - = - = - = - ")


def mainMethod():  # Главный метод
	bagCapacity = int(userInput())
	resultDict = addVariant(bagCapacity)
	showDict(resultDict)


mainMethod()
