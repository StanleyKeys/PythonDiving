"""
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""
import os.path


def createFileTuple(filePath):
	rev = ''.join(reversed(filePath))

	# Получаем расширение файла
	fileExtension = rev.partition('.')[0]

	# Имя файла (убрано расширение)
	fileName = ''.join(reversed(rev.partition('\\')[0])).replace(f'.{fileExtension}', '')

	# Сам кортеж
	resultTuple = (f'Path={filePath}', f'FileName={fileName}', f'FileExtension={fileExtension}')
	return resultTuple


def mainMethod():
	file = "testTuple.txt"
	filePath = os.path.abspath(file)
	resultTuple = createFileTuple(filePath)
	print(resultTuple)


mainMethod()
