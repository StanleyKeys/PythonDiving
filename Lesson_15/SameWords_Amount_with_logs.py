"""
Задание с Семинара №3 :
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
import logging

text = "Викинги - раннесредневековые скандинавские мореходы в VIII—XI веках, совершавшие морские походы от Винланда " \
       "до Биармии и Северной Африки. В основной массе это были племена (даны, свеи, гёты, гуты и др.) в стадии " \
       "разложения родоплеменного строя, жившие на территории современных Швеции, Дании и Норвегии, которых толкало " \
       "за пределы родных стран перенаселение и голод. По религиозной принадлежности викинги в подавляющем " \
       "большинстве были язычниками"


def clearText(text: str):  # Метод очистки текста от пунктуации.
    logging.info('The method "clearText" is working... ')
    text = text.replace(',', '').replace('.', '').replace('-', '').replace('(', '').replace(')', '')
    return text


def countWords(text: list):  # Метод подсчета одинаковых слов.
    logging.info('The method "countWords" is working... ')
    countDict = {}
    logging.warning("This method may take for a long time.")
    for element in text:
        if (countDict.get(element, None)):
            countDict[element] += 1
        else:
            countDict[element] = 1

    return countDict


def sortItemsOfDict(textDict: {}):  # Сортирует словарь по значениям и выводит от большего к меньшему
    logging.info('The method "sort_dict_items" is working... ')
    sortedDict = dict(sorted(textDict.items(), key=lambda word: word[1], reverse=True))
    return sortedDict


def showDict(dict: {}):  # Красивый вывод всех слов и их количества в тексте
    print("*** Список повторных слов ***")
    for element in dict:
        pointAmount = 30 - len(element) - 1
        pointAdd = pointAmount * '.'
        print(f'{element}{pointAdd}{dict[element]}')
    logging.info(f'The dict is: {dict}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="SameWords_Amount.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")

    t = clearText(text.lower())
    result = countWords(t.split())
    sortedItemResult = sortItemsOfDict(result)
    showDict(sortedItemResult)
