"""
Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.<br>
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.<br>
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

"""
import csv
import math
import random
from csv import writer


# Нахождение корней квадратного уравнения
def quadratic_root():
    print("Введите значения для квадратного уравнения \n"
          "ax^2 + bx + c = 0 \n")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    discriminant = b ** 2 - 4 * a * c
    print(f"Дискриминант D = {round(discriminant, 2)}")

    if (discriminant > 0):
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {round(x1, 2)} \n"
              f"x2 = {round(x2, 2)} \n")
    elif (discriminant == 0):
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("Корней нет")


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def random_CSV_file():
    randomRows = random.randint(100, 1000)
    counter = 0

    while (counter < randomRows):
        randomNumber = str(random.randint(100, 999))
        r = randomNumber[0] + randomNumber[2]
        with open('NumberCSVfile.csv', 'a', newline='') as file:
            fileWriter = writer(file, delimiter=randomNumber[1])
            fileWriter.writerow(r)
            file.close()
        counter += 1


def mainMethod():
    # quadratic_root()
    random_CSV_file()


mainMethod()
