"""
Напишите функцию, которая заполняет файл( добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой
Минимальное число = -1000, максимальное = 1000
Количество строк и имя файла передаются как аргументы функции
"""

from pathlib import Path
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def fill_numbers(count: int, fileName: str | Path) -> None:
	with open(fileName, 'a', encoding='utf-8') as file:
		for _ in range(count):
			file.write(f'{randint(MIN_NUM, MAX_NUM)}|{uniform(MIN_NUM, MAX_NUM)}\n')


def mainMethod():
	fill_numbers(1, "test.txt")
