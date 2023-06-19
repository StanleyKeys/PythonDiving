"""
Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

"""
import json
import csv
import math
import random
from csv import writer

quadraticDict: dict[str, list] = {}


# Нахождение корней квадратного уравнения
def quadratic_root(a: float, b: float, c: float):
    resultList = []
    discriminant = b ** 2 - 4 * a * c
    # print(f"Дискриминант D = {round(discriminant, 2)}")
    resultList.append(f"D = {round(discriminant, 2)}")
    if (discriminant > 0):
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        # print(f"x1 = {round(x1, 2)} \n"
        #       f"x2 = {round(x2, 2)} \n")
        resultList.append(f"x1 = {round(x1, 2)}")
        resultList.append(f"x2 = {round(x2, 2)}")
    elif (discriminant == 0):
        x = -b / (2 * a)
        # print(f"x = {x}")
        resultList.append(f"x = {x}")
    else:
        # print("Корней нет")
        resultList.append("No Roots")

    return resultList


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
"""
При сохранении трехзначного числа числа ставится ЗАПЯТАЯ через каждый символ
При сохранении списка трехзначных чисел ВСЕ ЭЛЕМЕНТЫ списка остаются в одной строке
Делаем пару хитростей:
1. Создаем список трехзначных чисел
2. Во время записи в CSV-файл сохраняем ЭЛЕМЕНТЫ через разделитель (delimimter='\n')
"""


def random_csv_file():
    numberList = []
    randomRows = random.randint(100, 1000)
    counter = 0

    while (counter < randomRows):
        randomNumber = str(random.randint(100, 999))
        numberList.append(randomNumber)
        counter += 1

    with open('NumberCSVfile.csv', 'a') as file:
        fileWriter = writer(file, delimiter="\n")
        fileWriter.writerow(numberList)
        file.close()


# Вторая функция, которая записывает именно ТРИ РАЗНЫХ ЧИСЛА в одну строку через запятую
"""
функция writerow() посимвольно записывает число в строку.
Например: число 754 будет записано как 7,5,4 в одну строку.
"""


def random_csv_file2():
    randomRows = random.randint(100, 1000)
    counter = 0

    while (counter < randomRows):
        randomNumber = str(random.randint(100, 999))

        with open('NumberCSVfile.csv', 'a', newline='') as file:
            fileWriter = writer(file)
            fileWriter.writerow(randomNumber)
            file.close()

        counter += 1


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def quadratic_csv_decorator(quadro_function):
    with open('NumberCSVfile.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            r = quadro_function(float(row[0]), float(row[1]), float(row[2]))
            quadraticDict[f'a={row[0]};b={row[1]};c={row[2]}'] = r


# Функиця, сохраняющая словарь в JSON-файл
def save_to_json(dict):
    with open("quadraticDict.json", "w", encoding="utf-8") as file:
        json.dump(dict, file)
        file.close()


# Функция-Декоратор, принимающая save_json-функцию и словарь
def decorator_save_json(saveJSON, dict):
    saveJSON(dict)


def mainMethod():
    # quadratic_root()
    # random_csv_file2()
    quadratic_csv_decorator(quadratic_root)
    decorator_save_json(save_to_json, quadraticDict)


mainMethod()
