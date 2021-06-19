# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import re


class Own_data:
    def __init__(self, user_str):
        self.user_str = user_str

    @classmethod  # первый способ - через список
    def get_number_from_data1(cls, user_data):
        re_user_str = re.compile(r'([0-9]+)-([0-9]+)-([0-9]+)')
        return [int(el) for el in re_user_str.findall(cls(user_data).user_str)[0]]

    @classmethod  # второй способ - через словарь
    def get_number_from_data2(cls, user_data):
        re_user_str = re.compile(r'(?P<dd>[0-9]+)-(?P<mm>[0-9]+)-(?P<yyyy>[0-9]+)')
        dict_out = [el for el in map(lambda x: x.groupdict(), re_user_str.finditer(cls(user_data).user_str))][0]
        dict_out = {key: int(val) for key, val in dict_out.items()}
        return dict_out

    @staticmethod  # первый способ - через список
    def check_number_from_data1(user_data):
        tmp = Own_data.get_number_from_data1(user_data)
        if tmp[0] == 0 or tmp[0] > 31:
            return f'Вы ввели не верное номер дня месяца'
        if tmp[1] == 0 or tmp[1] > 12:
            return f'Вы ввели не верный номер месяца'
        if tmp[2] == 0:
            return f'Вы ввели не верный номер года'

    @staticmethod  # второй способ - через словарь
    def check_number_from_data2(user_data):
        tmp = Own_data.get_number_from_data2(user_data)
        if tmp['dd'] == 0 or tmp['dd'] > 31:
            return f'Вы ввели не верное номер дня месяца'
        if tmp['mm'] == 0 or tmp['mm'] > 12:
            return f'Вы ввели не верный номер месяца'
        if tmp['yyyy'] == 0:
            return f'Вы ввели не верный номер года'


my_data = '12-34-2022'
print('Первый способ')
print(f'Строка даты "{my_data}" преобразованная в числа: {Own_data.get_number_from_data1(my_data)}')
print(f'Проверка даты - {Own_data.check_number_from_data1(my_data)}')
print('\nВторой способ')
print(f'Строка даты "{my_data}" преобразованная в числа: {Own_data.get_number_from_data2(my_data)}')
print(f'Проверка даты - {Own_data.check_number_from_data2(my_data)}')
