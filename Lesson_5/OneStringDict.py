"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии.
"""


def createOneStringGenerator(): # Метод генератора словаря в одну строку через лямбды
	list1 = ["Александр", "Евгений", "Валерия"]
	list2 = [5000, 4000, 6000]
	list3 = ['10.25%', '15.15%', '14.41%']

	dict1 = dict(zip(list1, [x * (float(y)/100) for x, y in zip(list2, [item.replace("%", "") for item in list3])]))
	return dict1


def createOneStringGenerator_2(): # Также в одну строку, но с изначальным обьединением всех списков вместе.
	list1 = ["Александр", 5000, '10.25%']
	list2 = ["Евгений", 4000, '15.15%']
	list3 = ["Валерия", 6000, '14.41%']
	list4 = list(zip(list1, list2, list3))

	dict1 = dict(zip(list4[0], [x * (float(y)/100) for x, y in zip(list4[1], [item.replace("%", "") for item in list4[2]])]))
	return dict1

def createOneStringGenerator_3():
	# Такой же метод что и "МЕТОД №2", но обьединением списков внутри лямбды (в одну строку)
	# Очень сложный в понимании и в написании. (я бы НЕ рекомендовал так делать)
	list1 = ["Александр", 5000, '10.25%']
	list2 = ["Евгений", 4000, '15.15%']
	list3 = ["Валерия", 6000, '14.41%']

	dict1 = dict(zip(list(zip(list1, list2, list3))[0], [x * (float(y)/100) for x, y in zip(list(zip(list1, list2, list3))[1], [item.replace("%", "") for item in list(zip(list1, list2, list3))[2]])]))
	return dict1


def mainMethod():
	print("Function #1 : ")
	result1 = createOneStringGenerator()
	print(result1)
	print()
	print("Function #2 : ")
	result2 = createOneStringGenerator_2()
	print(result2)
	print()
	print("Function #3 : ")
	result3 = createOneStringGenerator_3()
	print(result3)


mainMethod()


def test():
	list1 = ["Александр", 5, '10.25%']
	list2 = ["Евгений", 4, '15.15%']
	list3 = ["Валерия", 6, '14.41%']

	list4 = list(zip(list1, list2, list3))

	print(list4)


# test()
