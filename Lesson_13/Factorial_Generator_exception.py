"""
СТАРОЕ:
Задание 3 :
 Создайте класс-генератор.
- Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
- Если переданы два параметра, считаем step=1.
- Если передан один параметр, также считаем start=1.
"""
"""
НОВОЕ:
* Напишите к ним классы исключения с выводом подробной информации
"""

class MyArgsLenError(Exception):

    def __init__(self, text):
        self.txt = text

class Factorial:
    fact_list = []

    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start, self.stop, self.step = args
            case _:
                raise MyArgsLenError("Amount of arguments must be from 1 to 3")

    def __call__(self, value):
        result = []
        fact = 1
        for i in range(2, value + 1):
            fact *= i
            self.fact_list.append(fact)
        for j in range(self.start, self.stop, self.step):
            result.append(self.fact_list[j])
        return result


if __name__ == '__main__':
    fact = 1
    r = []
    for i in range(2, 8 + 1):
        fact *= i
        r.append(fact)
    print(r)

    f = Factorial(3, 6, 1)
    print(f(8))
