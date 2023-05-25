"""
Напишите программу банкомат
- Начальная сумма равна нулю
- Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
   операцией, даже ошибочной
- Любое действие выводит сумму денег
"""
import sys
import time
from datetime import date


def userInput():  # Ввод
	userEnter = input("Input the number: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def showBalance():  # Отображает баланс
	print(f'*** Ваш баланс: {atm.balance()} y.e. ***\n')


def chooseMenu():  # Главное меню
	showBalance()
	choice = input("Выберите действие \n"
	               "1. Пополнить Баланс \n"
	               "2. Снять наличные \n"
	               "3. Выход \n")
	match (choice):
		case '1':
			addCash()
		case '2':
			withdrawCash()
		case '3':
			exitATM()
		case _:
			print("Необходимо выбрать пункт меню \n")
			chooseMenu()



def addCash():  # Метод добавления средств
	cash = input("На какую сумму вы хотите пополнить: \n")
	atm.add(int(cash))


def withdrawCash():  # Метод снятия средств
	cash = input("Какую сумму желаете снять: \n")
	atm.withdraw(int(cash))


def exitATM():  # Выход
	atm.exit()


class ATM:
	_BALANCE = 0  # Баланс
	_MULTIPLICITY = 50  # Кратность пополнения/снятия
	_COMISSION = 0.015  # Комиссия за снятия средств
	_BONUS = 0.03  # бонус за пользование
	_TAX = 0.10  # налог на богатство
	_BONUS_COUNTER = 0  # Счетчик бонуса
	_TOTAL_INCOME = 0  # Общая прибыль (сделал из условий прибыли за месяц)
	_DateOfFirstAction = 0  # Дата первого действия по счету за месяц.

	def add(self, cash: int):  # Пополнение баланса
		self.checkDate()
		if (cash % self._MULTIPLICITY == 0):
			self._BALANCE += cash
			self._TOTAL_INCOME += cash
			print("--- Денежные средства успешно зачислены на счет --- \n")
			self._addBonus()
			self._checkTotalIncome()
			chooseMenu()
		else:
			print("* * * * * ОШИБКА! * * * * * \nСумма должна быть кратна 50 у.е.\n")
			self._checkTotalIncome()
			addCash()

	def withdraw(self, cash: int):  # Снятие со счета
		self.checkDate()
		if (cash % self._MULTIPLICITY == 0):
			withdrawPercent = cash * self._COMISSION
			if (withdrawPercent < 30):
				withdrawPercent = 30
			elif (withdrawPercent > 600):
				withdrawPercent = 600
			userChoice = input(f"Комиссия за снятие составляет: {withdrawPercent} y.e. \n"
			                   f"Продолжить? \n")
			if (userChoice == "1" or userChoice == "yes"):
				cash = cash + withdrawPercent
				if (cash <= self._BALANCE):
					self._BALANCE -= cash
					print("--- Денежные средства успешно сняты со счета --- \n")
				else:
					print("Сумма снятия с учетом комиссии превышает текущий баланс. \n"
					      "Попробуйте изменить сумму снятия \n")
					chooseMenu()
			elif (userChoice == "2" or userChoice == "no"):
				print("*** ОТМЕНА ОПЕРАЦИИ *** \n")
			self._checkTotalIncome()
			self._addBonus()
			chooseMenu()
		else:
			print("* * * * * ОШИБКА! * * * * * \nСумма должна быть кратна 50 у.е.\n")
			self._checkTotalIncome()
			chooseMenu()

	def exit(self):  # Выход из программы
		print("Выход из программы \n")

		print("...3... \n")
		time.sleep(1)
		print("...2... \n")
		time.sleep(1)
		print("...1... \n")
		time.sleep(1)
		print("Всего доброго!")
		sys.exit()

	def balance(self):  # Баланс
		return self._BALANCE

	def _addBonus(self):  # Добавление бонуса на счет
		self._BONUS_COUNTER += 1
		if (self._BONUS_COUNTER == 3):
			actionBonus = round(self._BALANCE * self._BONUS, 1)
			self._BALANCE += actionBonus
			self._TOTAL_INCOME += actionBonus
			print(f"За активность по вашему счету Вам было начислено {actionBonus} y.e. \n")
			self._BONUS_COUNTER = 0

	def _checkTotalIncome(self):  # Подсчет общей прибыли за месяц
		if (self._TOTAL_INCOME >= 5000000):
			taxAction = round(self._BALANCE * self._TAX, 1)
			self._BALANCE -= taxAction
			print(f"*** ВНИМАНИЕ *** \nВаша общая прибыль  от {self._DateOfFirstAction} составила {self._TOTAL_INCOME} у.е. \n"
			      "Согласно ст. №214-ФЗ, №362-ФЗ НК РФ 'О Порядке исчисления суммы налога на богаство' \n"
			      f"С вас было удержано 10% от суммы общего дохода = {taxAction} y.e. \n")

	def checkDate(self):  # Проверка текущей даты с датой первого действия по счету (необходимо для сброса TOTAL_INCOME)
		current_date = date.today()
		if (self._DateOfFirstAction == 0):
			self._DateOfFirstAction = date.today()
		elif (current_date.month > self._DateOfFirstAction.month) or (
				current_date.month < self._DateOfFirstAction.month and current_date.year > self._DateOfFirstAction.year):
			self._DateOfFirstAction = date.today()
			self._TOTAL_INCOME = 0


def mainMethod():
	chooseMenu()


atm = ATM()
mainMethod()
