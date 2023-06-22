"""
Задание 2 :
- Создайте класс Архив, который хранит пару свойств.
  Например, число или строку.
- При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
- list-архивы также являются свойствами экземпляра.
"""


class Archive:
    '''Данные каждого экземпляра класса сохраняется в списки keys & values'''
    keys = []
    values = []

    def __new__(cls, key: int, value: str):
        '''Сохранение аргументов в списки'''
        instance = super().__new__(cls)
        cls.keys.append(key)
        cls.values.append(value)
        return instance

    def __init__(self, key: int, value: str):
        '''Инициалиазация экземпляра класса'''
        self.key = key
        self.value = value


    def __repr__(self):
        return f'Archive({self.key}, {self.value})'

    def __str__(self):
        return f'Ключ: {self.key}, Значение: {self.value}'

if __name__ == '__main__':
    a_1 = Archive(1, "One")
    a_2 = Archive(2, "Two")

    print(f'{a_1.keys} {a_1.values}')
    print(f'{a_2.keys} {a_2.values}')

    print(a_1.__repr__())
    print(a_1)