"""
Задание с Семинара №1
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

import doctest
import unittest
import pytest


# Класс-функция unitTest
class MyTest(unittest.TestCase):

    def test_type(self):
        with self.assertRaises(TypeError):
            checkPrimeOrComposite(3.14)
            checkPrimeOrComposite('dsfgdgdfg')

    def test_value(self):
        self.assertRaises(ValueError, checkPrimeOrComposite, -1)


def checkPrimeOrComposite(value):  # Проверка на Простоту
    '''
    text
    >>> checkPrimeOrComposite(3.14)
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> checkPrimeOrComposite('dsfgdgdfg')
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'int' and 'str'
    >>> checkPrimeOrComposite(-1)
    Traceback (most recent call last):
    ...
    ValueError: Your number must be between 1 and 100k
    '''

    if (0 < value < 100000):
        k = 0
        for i in range(2, value // 2 + 1):
            if (value % i == 0):
                k = k + 1
        if (k <= 0):
            return f'Your number "{value}" is Prime'
        else:
            return f'Your number "{value}" is Composite'
    else:
        raise ValueError('Your number must be between 1 and 100k')


# Функция модуля pyTest
def test_pytype():
    with pytest.raises(TypeError):
        checkPrimeOrComposite(3.14)
        checkPrimeOrComposite('dsfgdgdfg')


# Функция модуля pyTest
def test_value():
    with pytest.raises(ValueError):
        checkPrimeOrComposite(-1)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    unittest.main(verbosity=2)
