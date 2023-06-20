"""
�������� �������, ������� �������� �� ���� ���������� � ���������� ������� � � ��� ��������� ����������.
���������� ������ ��������� � ����� json, csv � pickle. - ��� �������� �������� ���������� ������������ ����������.
- ��� ������� ������� ������� ���� ��� ��� ����������. - ��� ������ ��������� ��� ������ � ������, � ��� ����������
  ������ ������ � ��� � ������ ���� ��������� ������ � ����������.

"""
import os
import json
import csv
import pickle

dir_path = 'T:\Important\Projects\pythonProject\PythonDiving\Lesson_7'

fileData: dict[str, list] = {}
fileData['Files'] = []
fileData['Dirs'] = []


# ������� �������� ���� � ������� ���������� ���������� ���� �����, ������� � dir_path
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

            print('���������� � ', path + '\\' + fileName)
            createFileData(path + '\\' + fileName, level + 1)
            print('������������ � ', path)


class Recorder():
    # ���������� � JSON:
    def saveToJSON(self):
        with open("fileData.json", "w", encoding="utf-8") as file:
            json.dump(fileData, file)
            file.close()

    # ���������� � CSV:
    def saveToCSV(self):
        with open('fileData.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(('FileName', 'ParentDirectory', 'Size'))
            for file in fileData['Files']:
                writer.writerow((file['FileName'], file['ParentDirectory'], file['Size']))

            writer.writerow(('DirName', 'FileAmount', 'Size'))
            for dir in fileData['Dirs']:
                writer.writerow((dir['DirName'], dir['FileAmount'], dir['Size']))
            csvfile.close()

    # ��������� � Pickle:
    def saveToPickle(self):
        with open('pickleFileData.data', 'ab') as pickleFile:
            pickle.dump(fileData, pickleFile)
            pickleFile.close()


# ���������� ���� Pickle:
def showPickle():
    with open('pickleFileData.data', 'rb') as f:
        obj = pickle.load(f)
        print(obj)
        f.close()


def mainMethod():
    recorder = Recorder()
    createFileData(dir_path)
    print(fileData)

    recorder.saveToJSON()
    recorder.saveToCSV()
    recorder.saveToPickle()


# showPickle()


mainMethod()
