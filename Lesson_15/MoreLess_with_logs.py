"""
Задача с Семинара №1 :
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""
import random
import logging


def userInput():  # Ввод
    userEnter = input("Input the number: ")
    if (userEnter.isdigit()):
        logging.info(f'The user entered {userEnter}')
        return userEnter
    else:
        print("incorrect")
        logging.error(f'The user entered "{userEnter}"')
        return userInput()


def playGame(num, tries):
    if (tries == 0):
        print("Sorry. But you haven't got any tries. \nGAME OVER")
        logging.info("The user tried to play again, but he had no attempts left")
    else:
        print(f"\nYou have {tries} tries\n")
        logging.info(f"The user has {tries} tries")
        a = int(userInput())
        if (a == num):
            print(f"Yes! Thats it! \nMy number is {num} \nCongratulations!")
            logging.info(f"The user guessed right the number and finished the game")
        elif (a > num):
            print("Your number is bigger than mine")
            logging.info("User's number is bigger than AI")
            tries -= 1
            playGame(num, tries)
        elif (a < num):
            print("Your number is less than mine")
            logging.info("User's number is less than AI")
            tries -= 1
            playGame(num, tries)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="MoreLess_Logs.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    print("Hello! Im J.A.R.V.I.S! \nTry to beat me!")
    num = random.randint(0, 1000)
    tries = 10
    print(num)
    logging.info("The Game is starting")
    logging.info(f'AI number is "{num}"')
    playGame(num, tries)
