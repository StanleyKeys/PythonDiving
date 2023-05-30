"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

itemList = [1, 4, 7, 0, 2, 5, 8, 3, 5, 6, 7, 1, 7, 2, 6, 3, 5, 4, 8, 9, 1, 2, 3, 4, 5, 7, 16, 5, 4, 3, 2, 1, 0, 9, 19]


def searchDuplicates():     # Метод ищет дупликаты
	sortedList = sorted(itemList)
	result = []
	for i in sortedList:
		if (sortedList.count(i) > 1):
			if i not in result:
				result.append(i)

	return result


def removeDuplicates():     # Метод удаляет дупликаты из основного списка
	temp = []
	for x in itemList:
		if x not in temp:
			temp.append(x)
	return temp


def mainMethod():
	duplicateList = searchDuplicates()
	itemList = removeDuplicates()
	print(f'Duplicate List = {duplicateList}')
	print()
	print(f'New Item List List = {itemList}')


mainMethod()
