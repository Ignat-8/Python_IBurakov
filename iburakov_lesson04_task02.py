# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Можно ли, используя только методы класса str,
# решить поставленную задачу? Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того,
# в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

import requests


def currency_get(url):
    """
    Осоществляет парсинг xml данных с адреса url
    :param url:Адрес для считывания курса валют
    :return:Возвращает словарь валют с их курсом
    """
    response = requests.get(url)
    response = '_'.join(response.text.split("<NumCode>"))
    response = '_'.join(response.split("</NumCode>"))
    response = ''.join(response.split("<CharCode>"))
    response = '_'.join(response.split("</CharCode>"))
    response = ''.join(response.split("<Nominal>"))
    response = '_'.join(response.split("</Nominal>"))
    response = ''.join(response.split("<Name>"))
    response = '_'.join(response.split("</Name>"))
    response = ''.join(response.split("<Value>"))
    response = '_'.join(response.split("</Value>"))
    response = ''.join(response.split("</Valute>"))
    response = response.split("_")
    currency_dict_all = {}
    for i in range(0, len(response)-1, 6):
        NumCode = response[i+1]
        CharCode = response[i+2]
        Nominal = response[i+3]
        Name = response[i+4]
        Value = float(response[i+5].replace(',', '.'))
        currency_dict_all.update({CharCode: {"NumCode": NumCode, "Nominal": Nominal, "Name": Name, "Value": Value}})
    return currency_dict_all


def currency_rates(currency_input):
    """
    Осуществляет выборку параметров заданной валюты из общего словаря валют
    :param currency_input:Сокращенное название валюты
    :return:Словарь значений для этой валюты
    """
    if CURRENCY_DICT_ALL.get(currency_input):
        return CURRENCY_DICT_ALL[currency_input]
    else:
        return {"NumCode": None, "Nominal": None, "Name": None, "Value": None, "Date": None}


url = 'http://www.cbr.ru/scripts/XML_daily.asp'
CURRENCY_DICT_ALL = currency_get(url)
currency_input = ''

while currency_input != 'q':
    currency_input = input('Введите сокращенное название валюты или q для выхода: ')
    currency_dict = currency_rates(currency_input.upper())
    print(f'Курс валюты {currency_input.upper()} ({currency_dict["Name"]}) = {currency_dict["Value"]}')
