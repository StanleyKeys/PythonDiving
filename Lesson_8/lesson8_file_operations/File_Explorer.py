"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle. - Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория. - Для файлов сохраните его размер в байтах, а для директорий
  размер файлов в ней с учётом всех вложенных файлов и директорий.

"""
import os
import json
import csv
import pickle

dir_path = 'T:\Important\Projects\pythonProject\PythonDiving\Lesson_7'

fileData: dict[str, list] = {}
fileData['Files'] = []
fileData['Dirs'] = []


# Сначала создадим базу и получим рекурсивно содержимое всех папок, начиная с dir_path
def createFileData(path, level=1):
    print('Level=', level, 'Content:', os.listdir(path))
    for fileName in os.listdir(path):
        fileAmount = 0
        sumSize = 0
        file = os.path.join(path, fileName)
        if os.path.isfile(file):
            size = os.path.getsize(file)
            fileData['Files'].append({
                'FileName': fileName,
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
            createFileData(path + '\\' + fileName, level + 1)
            print('Возвращаемся в ', path)


# Записываем в JSON:
def saveToJSON():
    with open("fileData.json", "w", encoding="utf-8") as file:
        json.dump(fileData, file)
        file.close()


# Записываем в CSV:
def saveToCSV():
    with open('fileData.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('FileName', 'ParentDirectory', 'Size'))
        for file in fileData['Files']:
            writer.writerow((file['FileName'], file['ParentDirectory'], file['Size']))

        writer.writerow(('DirName', 'FileAmount', 'Size'))
        for dir in fileData['Dirs']:
            writer.writerow((dir['DirName'], dir['FileAmount'], dir['Size']))
        csvfile.close()


# Сохраняем в Pickle:
def saveToPickle():
    with open('pickleFileData.data', 'ab') as pickleFile:
        pickle.dump(fileData, pickleFile)
        pickleFile.close()


# Отобразить файл Pickle:
def showPickle():
    with open('pickleFileData.data', 'rb') as f:
        obj = pickle.load(f)
        print(obj)
        f.close()


def mainMethod():
    createFileData(dir_path)
    print(fileData)

    saveToJSON()
    saveToCSV()
    saveToPickle()

# showPickle()



mainMethod()
