"""
Задание 5 :
- Дорабатываем класс прямогольник из прошлого семинара.
- Добавьте возможность сложения и вычитания.
- При этом должен создаваться новый экземпляр прямоугольника.
- Складываем и вычитаем периметры, а не длину и ширину.
- При вычитании не допускайте отрицательных значений.
"""


class Rectangle:

    def __init__(self, a: int, b: int = None):
        '''Инициализация класса'''
        self.a = a
        self.b = b if b is not None else a

    def perimeter(self):
        '''Подсчет периметра фигуры'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Подсчет площади фигуры'''
        return self.a * self.b

    def sum_perimeters(self, other):
        '''Складываем периметры двух фигур и возвращаем новую фигуру со сторонами'''
        rect_1 = self.perimeter()
        rect_2 = other.perimeter()
        new_rectangle_perimeter = rect_1 + rect_2
        new_rectangle_a = self.a + other.a
        new_rectangle_b = int(new_rectangle_perimeter / 2 - new_rectangle_a)
        return Rectangle(new_rectangle_a, new_rectangle_b)

    def sub_perimeters(self, other):
        '''Вычитаем периметры двух фигур и возвращаем новую фигуру со сторонами'''
        rect_1 = self.perimeter()
        rect_2 = other.perimeter()
        new_rectangle_perimeter = rect_1 - rect_2
        if (new_rectangle_perimeter >= 4):
            new_rectangle_a = self.a - other.a
            new_rectangle_b = int(new_rectangle_perimeter / 2 - new_rectangle_a)
            return Rectangle(new_rectangle_a, new_rectangle_b)
        else:
            print('Incorrect sides of Rectangle. Must be bigger than 1 cm for side')
            return Rectangle(0)


    def compareAreas(self, other):
        '''Сравнение двух фигур по площади'''
        rect_1 = self.area()
        rect_2 = other.area()
        if (rect_1 > rect_2):
            return f'{rect_1} > {rect_2}'
        elif (rect_1 < rect_2):
            return f'{rect_1} < {rect_2}'
        elif (rect_1 == rect_2):
            return f'{rect_1} == {rect_2}'


if __name__ == '__main__':
    rect_1 = Rectangle(9)
    rect_2 = Rectangle(4, 5)

    print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    print(f'{rect_2.perimeter()= } {rect_2.area()= }')

    rect_3 = rect_1.sum_perimeters(rect_2)
    print(f'{rect_3.perimeter()= } {rect_3.area()= }')

    rect_4 = rect_1.sub_perimeters(rect_2)
    print(f'{rect_4.perimeter()= } {rect_4.area()= }')

    print(rect_1.compareAreas(rect_2))
