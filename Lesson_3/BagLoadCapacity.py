"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

campItems = {
	"Палатка": 3,
	"Тент": 2,
	"Топор": 3,
	"Складная пила": 2,
	"Газовка": 3,
	"Котелок": 1,
	"Чайник": 1,
	"Миска": 1,
	"Универсальный нож": 1,
	"Разделочная доска": 1,
	"Решетка гриль": 1,
	"Ведро": 2,
	"Веревка": 2,
	"Аптечка": 3,
	"Аккумулятор": 1,
	"Телефон": 1
}

testDict = {
	"Вариант 1": ["Топор", "Чайник", "Телефон"],
	"Вариант 2": ["Кирка", "Котелок", "Веревка"],
	"Вариант 3": ["Аккумулятор", "Миска", "Ведро"]
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


def createBagVariants(bagCapacity):
	return -1
def addVariant(bagCapacity):
	variantAmount = 1
	resultDict = {}
	itemList = []
	tempList = []
	weight = bagCapacity
	while (variantAmount <= 5):
		for element in campItems:
			if (campItems[element] <= weight):
				itemList.append(element)
				weight -= campItems[element]
		resultDict[f"Вариант №{variantAmount}"] = itemList
		variantAmount += 1
		weight = bagCapacity
		itemList = tempList
	return resultDict


def showDict(dict):
	for element in dict:
		print(element)
		print(dict[element])


def mainMethod():
	bagCapacity = userInput()
	resultDict = createBagVariants(int(bagCapacity))



mainMethod()
