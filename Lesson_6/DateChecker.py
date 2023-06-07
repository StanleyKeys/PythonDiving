"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from datetime import datetime


def userInput():  # Ввод даты пользователем
	userEnter = input("Введите дату для проверки: \n")
	if ('/' in userEnter):
		return ".".join(userEnter.split("/"))
	else:
		return userEnter


def checkLeapYear(date: str) -> bool:  # Проверка
	CHECK_NORMAL_1 = 4
	CHECK_NORMAL_2 = 100
	CHECK_NORMAL_3 = 400
	YEARS = range(1, 10000)
	year = int(date.split(".")[-1])
	if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
		return True
	return False


def checkYear(year: str) -> bool:  # Проверка даты
	try:
		_ = datetime.strptime(year, "%d.%m.%Y").date()
		return True
	except:
		return False


def dateValidator(date: str) -> str:
	if checkYear(date):
		return "Високосный" if checkLeapYear(date) else "Не является високосным"
	else:
		return f"Дата некорректна"


def mainMethod():
	userDate = userInput()
	print(dateValidator(userDate))


mainMethod()
