"""
Создайте класс Матрица. Добавьте методы для:
- вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""


class Matrix:
    matrix = []

    def __init__(self, x: int, y: int):
        ''' Создание двумерного массива (матрицы) где х - кол-во строк, y = кол-во столбцов '''
        self.matrix = [0] * x
        for i in range(x):
            self.matrix[i] = [0] * y

    def show(self):
        ''' Красивый вывод матрицы пользователю '''
        for row in range(0, len(self.matrix)):
            print(self.matrix[row])

    def replace(self, row: int, col: int, value: int):
        ''' Замена элемента где: row - строка, col - столбец, value - новое значение '''
        self.matrix[row][col] = value

    def replaceAll(self, old_value: int, new_value: int):
        ''' Замена всех одинаковых значений '''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == old_value:
                    self.matrix[i][j] = new_value

    def compare(self, other):
        ''' Сравнение двух матриц. НЕ равны если разные элементы и если разный размер. '''
        return 'Матрицы равны' if self.matrix == other.matrix else 'Матрицы не равны'

    def sum_matrix(self, other):
        ''' Сложение двух матриц '''
        a = len(self.matrix) if len(self.matrix) >= len(other.matrix) else len(other.matrix)
        temp = Matrix(a, a)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                temp.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return temp

    def multiply_matrix(self, other):
        ''' Умножение элементов двух матриц '''
        a = len(self.matrix) if len(self.matrix) >= len(other.matrix) else len(other.matrix)
        temp = Matrix(a, a)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                temp.matrix[i][j] = self.matrix[i][j] * other.matrix[i][j]
        return temp


if __name__ == '__main__':
    print('m1: ')
    m1 = Matrix(5, 4)
    m1.replace(2, 2, 5)
    # m.replace(1, 1, 5)
    # m.replace(0, 0, 5)
    m1.show()
    print()
    print('m2: ')
    m2 = Matrix(5, 5)
    m2.replace(2, 2, 5)
    # m.replaceAll(5, 7)
    m2.show()
    print()
    print(f'm1 & m2 : {m1.compare(m2)}')
    print()
    print('m3: sum m1 & m2')
    m3 = m1.sum_matrix(m2)
    m3.show()
    print()
    print('m4: multi m1 & m2')
    m4 = m1.multiply_matrix(m2)
    m4.show()
