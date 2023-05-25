"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

"""


def userInput():  # Ввод
	userEnter = input("Input the number: ")
	if (userEnter.isdigit()):
		return userEnter
	else:
		print("incorrect")
		return userInput()


def toHex(a):
	s = ""
	result = "0x"
	while True:
		s += "0123456789ABCDEF"[a % 16]
		a //= 16
		if a == 0:
			return result + ''.join(reversed(s))


def mainMethod():
	a = int(userInput())

	h1 = hex(a)
	h2 = ("%#x" % a)
	h3 = f'0x{a:x}'
	h4 = format(a, '#x')
	h5 = toHex(a)

	print(f'h1 = {h1}')
	print(f'h2 = {h2}')
	print(f'h3 = {h3}')
	print(f'h4 = {h4}')
	print(f'h5 = {h5}')

mainMethod()
