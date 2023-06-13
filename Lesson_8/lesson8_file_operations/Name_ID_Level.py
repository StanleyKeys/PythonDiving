"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7)
- После каждого ввода добавляйте новую информацию в JSON файл
- Пользователи группируются по уровню доступа.
- Идентификатор пользователя выступает ключом для имени.
- Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
- При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
import os.path
import json

# Создаем Слоравь
userData = {}


def create_user_dict():
    for i in range(1, 8):
        userData[f'Access_Level N{i}'] = []


# Получаем данные от пользователя
def getName_ID_Level(userData):
    userInput = input("Введите через пробел Имя, личный идентификатор, и уровень доступа от 1 до 7: \n").split(" ")
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
        saveToJSON(userData)


# Сохраняем в JSON
def saveToJSON(userData):
    with open('userData.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(userData, ensure_ascii=False))
        file.close()


# Подгружаем JSON-файл если есть
def loadFromJSON():
    if os.path.exists('userData.json'):
        with open('userData.json', 'r', encoding='utf-8') as file:
            result = json.load(file)
            file.close()
        return result


# Главный метод
def mainMethod():
    create_user_dict()
    userData = loadFromJSON()
    counter = 0
    while (counter < 5):
        getName_ID_Level(userData)
        counter += 1
    print(userData)


mainMethod()
