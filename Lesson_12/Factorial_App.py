"""
Задание 1 :
 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
- Экземпляр должен запоминать последние k значений.
- Параметр k передается при создании экземпляра.
- Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
"""


class Factorial:
    save_list = []

    def __init__(self, k: int):
        self.k = k

    def __call__(self, value):
        fact = 1
        for i in range(2, value + 1):
            fact *= i
        self.save_list.append(fact)
        return self.save_list[self.k - 1:-1]


if __name__ == '__main__':
    fact = Factorial(5)
    print(fact(3))
    print(fact(4))
    print(fact(5))
    print(fact(6))
    print(fact(7))
    print(fact(8))
    print(fact(9))
    print(fact(10))

    
