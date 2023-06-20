"""
�������� �������, ������� � ����������� ����� ����������� ���, ������ ������������� � ������� ������� (�� 1 �� 7)
- ����� ������� ����� ���������� ����� ���������� � JSON ����
- ������������ ������������ �� ������ �������.
- ������������� ������������ ��������� ������ ��� �����.
- ���������, ��� ��� �������������� ��������� ���������� �� ������ �������.
- ��� ����������� ������� ��� ���������� � ���� ������ ������ �����������.
"""
import os.path
import json


def create_user_dict():
    for i in range(1, 8):
        Json_Worker.userData[f'Access_Level N{i}'] = []


# �������� ������ �� ������������
def getName_ID_Level(userData):
    userInput = input("������� ����� ������ ���, ������ �������������, � ������� ������� �� 1 �� 7: \n").split(" ")
    userName = userInput[0]
    userID = userInput[1]
    userLevel = userInput[2]
    if (int(userLevel) < 1 or int(userLevel) > 7):
        print('incorrect Access_Level. Try Again \n')
        getName_ID_Level()
    else:
        userData[f'Access_Level N{userLevel}'].append({
            f'ID_{userID}': f'{userName}'
        })
        Json_Worker.saveToJSON(userData)


class Json_Worker():
    # ������� �������
    userData = {}

    # ��������� � JSON
    def saveToJSON(self, userData):
        with open('userData.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(userData, ensure_ascii=False))
            file.close()

    # ���������� JSON-���� ���� ����
    def loadFromJSON(self):
        if os.path.exists('userData.json'):
            with open('userData.json', 'r', encoding='utf-8') as file:
                result = json.load(file)
                file.close()
            return result


# ������� �����
def mainMethod():
    jsonWorker = Json_Worker()
    create_user_dict()
    userData = jsonWorker.loadFromJSON()
    counter = 0
    while (counter < 5):
        getName_ID_Level(jsonWorker.userData)
        counter += 1
    print(jsonWorker.userData)


mainMethod()
