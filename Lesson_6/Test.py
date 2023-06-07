"""
Создайте программу для игры в ""Крестики-нолики"".
"""

import random

import os                                                           # Код
clear = lambda: os.system('cls')                                    # очистки
clear()                                                             # терминала

input('         Добро Пожаловать в игру "Крестики-нолики"! \
    \n          Для продолжения нажмите любую клавишу ')
#=============================================================      # Рисование матрицы
def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for i2 in range(0, len(matrix[i])):
            print(matrix[i][i2], end=" ")
        print()

#=============================================================      # Проверка на ввод
def InputNumbers():
    is_OK = False
    while not is_OK:
        try:
            number = int(input("Введите номер строки:  ")) - 1, int(input("Введите номер столбца: ")) - 1
            is_OK = True
        except ValueError:
            print("Это неправильные циферки!")
    return number

#============================================================       # Проверка на повторение чисел
def check_num(number, temp_area):
    is_OK = False
    while not is_OK:
        if 0 <= number[0] < 3 and 0 <= number[1] < 3:
            if [i for i in temp_area if i == number]:
                print("Уже было")
                number = InputNumbers()
            else:
                is_OK = True
        else:
            print("Вне пределов доски.")
            number = InputNumbers()
    return number

#============================================================       # Нолик
def get_o(temp_area):
    number = (0, 0)
    while [i for i in temp_area if i == number]:
        number = (random.randint(0, 2), random.randint(0, 2))
    return number

#===========================================================        # Результат матрицы
def check_result(matrix, liter):
    x = ""
    if (
        matrix[0][0] == matrix[0][1] == matrix[0][2] == str(liter)
        or matrix[1][0] == matrix[1][1] == matrix[1][2] == str(liter)
        or matrix[2][0] == matrix[2][1] == matrix[2][2] == str(liter)
        or matrix[0][0] == matrix[1][0] == matrix[2][0] == str(liter)
        or matrix[0][1] == matrix[1][1] == matrix[2][1] == str(liter)
        or matrix[0][2] == matrix[1][2] == matrix[2][2] == str(liter)
        or matrix[0][0] == matrix[1][1] == matrix[2][2] == str(liter)
        or matrix[0][2] == matrix[1][1] == matrix[2][0] == str(liter)
    ):
        x = str(liter)
    return x

#===========================================================
area = []
area = [["."] * 3 for i in range(3)]
fill_aria = area
temp_area = []
print_matrix(area)

while len(temp_area) < 9:
    num = InputNumbers()
    num_x = check_num(num, temp_area)
    temp_area.append(num_x)
    fill_aria[num_x[0]][num_x[1]] = "x"
    print_matrix(fill_aria)
    result = check_result(fill_aria, "x")
    if result == "x":
        print("YOU WIN !")
        break
    if len(temp_area) == 9:
        break
    num_o = get_o(temp_area)
    print(f"Ход противника: {num_o[0]+1, num_o[1]+1}")
    temp_area.append(num_o)
    fill_aria[num_o[0]][num_o[1]] = "o"
    print_matrix(fill_aria)
    result = check_result(fill_aria, "o")
    if result == "o":
        print("YOU LOST :(")
        break
print("GAME OVER")