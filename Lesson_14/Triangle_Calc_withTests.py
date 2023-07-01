"""
Задание с Семинара №1:
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""
import doctest
import unittest


class MyTest(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            checkTriangleForm("a", "b", "c")
            userInput("HelloWorld")

    def test_triangleForm(self):
        self.assertEqual(checkTriangleForm(10, 5, 2), 'Triangle is VERSATILE')
        self.assertEqual(checkTriangleForm(5, 5, 5), 'Triangle is EQUILATERAL')
        self.assertEqual(checkTriangleForm(5, 5, 7), 'Triangle is ISOSCELES')


def userInput(userEnter):  # Ввод сторон пользователем
    # userEnter = input("Input the number of side: ")
    if (userEnter.isdigit()):
        return userEnter
    else:
        raise TypeError('Value must be integer')


def checkSides(a, b, c):  # Проверка сторон на существующий треугольник
    '''
    >>> checkSides(10, 5, 2)
    no such triangle exists
    '''
    if (a > b + c or b > a + c or c > a + b):
        print("no such triangle exists")
    else:
        checkTriangleForm(a, b, c)


def checkTriangleForm(a, b, c):  # Проверка формы треугольника
    '''

    >>> checkTriangleForm("a", "b", "c")
    Traceback (most recent call last):
    ...
    ValueError: Sides "a", "b", "c" must be integer or float
    >>> checkTriangleForm(10, 5, 2)
    Triangle is VERSATILE
    >>> checkTriangleForm(5, 5, 5)
    Triangle is EQUILATERAL
    >>> checkTriangleForm(5, 5, 7)
    Triangle is ISOSCELES
    '''
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        if (a == b and a == c):
            return f"Triangle is EQUILATERAL"  # Равносторонний
        elif (a == b or a == c or b == c):
            return f"Triangle is ISOSCELES"  # Равнобедренный
        elif (a != b and a != c and b != c):
            return f"Triangle is VERSATILE"  # Разносторонний
    else:
        raise TypeError('Sides "a", "b", "c" must be integer or float')


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
