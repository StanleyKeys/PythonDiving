"""
Напишите функцию для транспонирования матрицы
"""

matrix = [[1, 2, 3], [4, 5, 6]]


def transponseMatrix(matrix):
	result = []
	n = len(matrix)
	m = len(matrix[0])
	for i in range(m):
		temp = []
		for j in range(n):
			temp = temp + [matrix[j][i]]
		result = result + [temp]
	return result


def showMatrix(matrix):
	for i in matrix:
		print(i)


print("Old Matrix")
showMatrix(matrix)
result = transponseMatrix(matrix)
print("New Matrix")
showMatrix(result)
