"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

text = "Викинги - раннесредневековые скандинавские мореходы в VIII—XI веках, совершавшие морские походы от Винланда " \
       "до Биармии и Северной Африки. В основной массе это были племена (даны, свеи, гёты, гуты и др.) в стадии " \
       "разложения родоплеменного строя, жившие на территории современных Швеции, Дании и Норвегии, которых толкало " \
       "за пределы родных стран перенаселение и голод. По религиозной принадлежности викинги в подавляющем " \
       "большинстве были язычниками"


def clearText(text: str):  # Метод очистки текста от пунктуации.
	text = text.replace(',', '').replace('.', '').replace('-', '').replace('(','').replace(')','')
	return text


def countWords(text: list):  # Метод подсчета одинаковых слов.
	countDict = {}
	for element in text:
		if (countDict.get(element, None)):
			countDict[element] += 1
		else:
			countDict[element] = 1

	"""
		Можно вернуть отсортированный словарь слов:
		sortedDict = sorted(countDict.items(), key=lambda tpl: tpl[1], reverse=True) 
	"""
	return countDict


def showDict(dict: {}):
	print("*** Список повторных слов ***")
	for element in dict:
		pointAmount = 30 - len(element) - 1
		pointAdd = pointAmount * '.'
		print(f'{element}{pointAdd}{dict[element]}')


def mainMethod():  # Главный метод
	t = clearText(text.lower())
	result = countWords(t.split())
	showDict(result)


mainMethod()
