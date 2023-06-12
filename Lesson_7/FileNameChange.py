"""
Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os

dirPath = "T:\Important\Projects\pythonProject\PythonDiving\Lesson_7"


def changeFileName(finalName: str, amount: int, extensionOfFiles: str,
                   finalFileExtension: str, startRange: int, endRange: int):
	# Берем счетчик
	counter = 0

	# Открываем папку из пути, и перебираем файлы
	for root, dirs, files in os.walk(dirPath):
		for file in files:
			if (counter != amount):
				fileNameList = file.split(".")
				extension = fileNameList[len(fileNameList) - 1]

				# Если диапазон в параметрах выбран нулевой(вычитаем 1, чтоб получить отрицательный элемент списка),
				# то к новому названию файла ничего не добавляется.
				if (startRange - 1 == -1 and endRange - 1 == -1):
					changedName = ""
				else:
					changedName = file[startRange:endRange]
				# Если расширения совпадают то делаем изменения в названии и расширении
				if (extension == extensionOfFiles):
					if (counter == 0):
						os.rename(file, changedName + finalName + "." + finalFileExtension)
						counter += 1
					# Добавляем счетчик (как в 'Windows' при дубликатах)
					elif (counter > 0):
						os.rename(file, changedName + finalName + f"({counter})." + finalFileExtension)
						counter += 1


def mainMethod():
	changeFileName(finalName="world", amount=5, extensionOfFiles="txt",
	               finalFileExtension="txt", startRange=3, endRange=6)


mainMethod()
