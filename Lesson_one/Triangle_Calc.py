'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
'''


def userInput():                # Ввод сторон пользователем
	userEnter = input("Input the number of side: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def checkSides(a, b, c):        # Проверка сторон на существующий треугольник
	if (a > b + c or b > a + c or c > a + b):
		print("no such triangle exists")
	else:
		checkTriangleForm(a, b, c)


def checkTriangleForm(a, b, c): # Проверка формы треугольника
	if (a == b and a == c):
		print(f"Sides: \n a = {a}\n b = {b}\n c = {c}\n Triangle is EQUILATERAL")  # Равносторонний
	elif (a == b or a == c or b == c):
		print(f"Sides: \n a = {a}\n b = {b}\n c = {c}\n Triangle is ISOSCELES")  # Равнобедренный
	elif (a != b and a != c and b != c):
		print(f"Sides: \n a = {a}\n b = {b}\n c = {c}\n Triangle is VERSATILE")  # Разносторонний


def mainMethod():               # Главный метод
	a = int(userInput())
	b = int(userInput())
	c = int(userInput())
	checkSides(a, b, c)


mainMethod()
