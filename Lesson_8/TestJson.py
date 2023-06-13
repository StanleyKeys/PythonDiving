"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. - Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория. - Для файлов сохраните его размер в байтах, а для директорий
  размер файлов в ней с учётом всех вложенных файлов и директорий.

"""
import os
import json

dir_path = 'T:\Important\Projects\pythonProject\PythonDiving\Lesson_7'

fileData = {}
fileData['Files'] = []
fileData['Dirs'] = []


def saveToJSON(path, level=1):
	print('Level=', level, 'Content:', os.listdir(path))
	for fileName in os.listdir(path):
		fileAmount = 0
		sumSize = 0
		file = os.path.join(path, fileName)
		if os.path.isfile(file):
			size = os.path.getsize(file)
			fileData['Files'].append({
				'fileName': fileName,
				'ParentDirectory': path,
				'Size': size
			})
			fileAmount += 1
			sumSize += size
		if os.path.isdir(path + '\\' + fileName):
			fileData['Dirs'].append({
				'DirName': path,
				'FileAmount': len(os.listdir(path)),
				'Size': os.path.getsize(path)
			})

			print('Спускаемся в ', path + '\\' + fileName)
			saveToJSON(path + '\\' + fileName, level + 1)
			print('Возвращаемся в ', path)


def mainMethod():
	saveToJSON(dir_path)
	print(fileData)


mainMethod()
