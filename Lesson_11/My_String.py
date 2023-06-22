"""
Задание 1 :
- Создать класс MY String, где:
- будут доступны все возможности str
- дополнительно хранятся имя автора строки и время создания (time.time)
"""
import time
class MyString(str):
    '''метод расширяет new параметрами value и name'''
    def __new__(cls, value: str, name: str):
        instance = super().__new__(cls)

        instance.name = name
        instance.created_at = time.time()
        return instance


if __name__ == '__main__':
    mystr = MyString('сама строка', 'доп. параметр')
    print(mystr.name)
    print(mystr.created_at)