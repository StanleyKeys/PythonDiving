"""
Задание с Семинара №2 :
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
import logging


def userInput():  # Ввод
    userEnter = input("Input the number: ")
    if (len(userEnter) >= 3):
        logging.info(f'The User entered {userEnter}')
        return userEnter
    else:
        print("incorrect")
        logging.error(f'The User entered {userEnter}')
        return userInput()


def sumFraction(a, b, aMark, bMark):  # Метод сложения дробей
    logging.info("Starting sum_fraction method...")
    aNumerator = int(a[len(a) - 3])
    bNumerator = int(b[len(b) - 3])
    aDenominator = int(a[len(a) - 1])
    bDenominator = int(b[len(b) - 1])
    c = f'{aMark * (aNumerator * bDenominator) + bMark * (bNumerator * aDenominator)}/{aDenominator * bDenominator}'
    logging.info(f'Fraction {a} + Fraction {b} = {c}')
    return c


def multiplyFractions(a, b, aMark, bMark):  # Метод умножения дробей
    logging.info("Starting multiply_fraction method...")
    aNumerator = int(a[len(a) - 3])
    bNumerator = int(b[len(b) - 3])
    aDenominator = int(a[len(a) - 1])
    bDenominator = int(b[len(b) - 1])
    c = f'{aMark * bMark * (aNumerator * bNumerator)}/{aDenominator * bDenominator}'
    logging.info(f'Fraction {a} * Fraction {b} = {c}')
    return c


def chooseAction(a, b):  # Выбор действия
    choice = input("Choose action with fractions:\n"
                   "1. Summ\n"
                   "2. Multiply\n")
    aMark = checkNegative(a)
    bMark = checkNegative(b)
    match (choice):
        case "1":
            logging.info('MAIN_MENU: The user chose 1')
            return sumFraction(a, b, aMark, bMark)
        case "2":
            logging.info('MAIN_MENU: The user chose 2')
            return multiplyFractions(a, b, aMark, bMark)


def checkNegative(fraction):
    if (fraction[0] == "-"):
        return -1
    else:
        return 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="Fractions_logs.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    a = userInput()
    b = userInput()

    c = chooseAction(a, b)
    print(f'Your answer is: {c}')
