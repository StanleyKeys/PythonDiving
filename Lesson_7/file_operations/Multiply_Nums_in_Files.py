"""
�������� �������, ������� ��������� �� ������ ��������� � ������� ������� ����� � ������� � �������.
����������� ���� �����. � ����� ���� ��������� ��� � ������������:
- ���� ��������� ��������� �������������, ��������� ��� ���������� ��������� �������, � ������������ �� ������.
- ���� ��������� ��������� �������������, ��������� ��� ���������� ������� � ������������ ����������� �� ������.
� �������������� ����� ������ ���� ������� �� �����, ������� � ����� ������� �����.
��� ���������� ����� ����� ��������� �����, ������������� � ��� ������.
"""

from pathlib import Path
from typing import TextIO


def _readOrBegin(fd: TextIO) -> str:
	line = fd.readline()
	if not line:
		fd.seek(0)
		return _readOrBegin(fd)
	return line[:-1]


def twoFilesInOne(numbers: Path, words: Path, result: Path) -> None:
	with (open(numbers, 'r', encoding='utf-8') as file_num,
	      open(words, 'r', encoding='utf-8') as file_word,
	      open(result, 'w', encoding='utf-8') as file_result
	      ):
		lenNumbers = sum(1 for _ in file_num)
		lenWord = sum(1 for _ in file_word)
		for _ in range(max(lenNumbers, lenWord)):
			num = _readOrBegin(file_num)
			word = _readOrBegin(file_word)
			numA, numB = num.split('|')
			multy = int(numA) + float(numB)
			if (multy < 0):
				file_result.write(f'{word.lower()}{abs(multy)}\n')
			elif (multy > 0):
				file_result.write(f'{word.upper()}{abs(multy)}\n')
