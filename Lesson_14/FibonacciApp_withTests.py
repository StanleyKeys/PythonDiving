"""
Задание с Семинара №4:
Создайте функцию генератор чисел Фибоначчи (см. Википедию)
"""
import doctest
import unittest


class MyTest(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            fib("HelloWorld")
            fib(3.14)
            userInput('Hello World')


def userInput(userEnter):  # Ввод
    # userEnter = input("Input the number: ")

    if (userEnter.isdigit()):
        return userEnter
    else:
        raise TypeError('Value must be integer')


def fib(userNumber):  # Метод вычисления порядка Фибоначчи
    '''
    Проверяем на тип данных:
    >>> fib("HelloWorld")
    Traceback (most recent call last):
        ...
    TypeError: 'str' object cannot be interpreted as an integer
    >>> fib(3.14)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer

    >>> userInput("Python VS Java")
    Traceback (most recent call last):
        ...
    TypeError: 'str' object cannot be interpreted as an integer
	'''
    fib1 = fib2 = 1
    print(fib1, fib2, end=' ')
    for i in range(2, userNumber):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
