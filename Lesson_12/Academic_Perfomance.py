"""
Создайте класс студента.
* Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
* Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
* Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
* Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""

import csv


class Descriptor:
    def __init__(self):
        self.__fio = ""

    def __get__(self, instance, owner):
        return self.__fio

    def __set__(self, instance, value):
        string_list = value.split(" ")

        for word in string_list:
            if word.isalpha():
                if word.istitle():
                    continue
                else:
                    raise ValueError("FIO must be with a Title chars")
            else:
                raise ValueError("FIO must be with only alphabet symbols")
        self.__fio = value


class Student:
    fio = Descriptor()

    def __init__(self, fio):
        self.fio = fio
        self.subject_list = self.get_subject_list()
        self.test_list = self.get_test_list()

    def __str__(self):
        return f'Student: {self.fio} \n' \
               f'Subjects: {self.subject_list[0]} \n' \
               f'Total Average: {self.subject_list[1]} \n' \
               f'Tests: {self.test_list[0]} \n' \
               f'Test Average: {round(self.test_list[1], 1)}'

    def get_subject_list(self):
        academic_progress = ""
        subj_counter = 0
        test_average = 0
        with open('subjects.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                subj_counter += 1
                temp_list = row[0].split(";")
                average = self.count_average(temp_list[1:])
                test_average += average
                academic_progress += f"\n{temp_list[0]}: {temp_list[1:]} - Average: {average}"
        test_average = test_average / subj_counter
        return [academic_progress, round(test_average, 1)]

    def get_test_list(self):
        test_progress = ""
        subj_counter = 0
        subj_average = 0
        with open('tests.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                subj_counter += 1
                temp_list = row[0].split(";")
                average = self.count_average(temp_list[1:])
                subj_average += average
                test_progress += f"\n{temp_list[0]}: {temp_list[1:]} - Average: {average}"
        subj_average = subj_average / subj_counter
        return [test_progress, subj_average]

    def count_average(self, list):
        result = 0
        for number in list:
            result += int(number)
        result = result / len(list)
        return round(result, 1)


if __name__ == '__main__':
    student1 = Student("Иванов Иван Иванович")
    print(student1)
