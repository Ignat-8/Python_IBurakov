# * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
# в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?

import requests
from requests import utils
from datetime import datetime

def currency_get(url):
    """
    Осоществляет парсинг xml данных с адреса url
    :param url:Адрес для считывания курса валют
    :return:Возвращает словарь валют с их курсом
    """
    response = requests.get(url)
    date_from_header = response.headers['Date'].split(' ')
    date_from_header = [date_from_header[1], date_from_header[2], date_from_header[3]]
    date_from_header = datetime.strptime(' '.join(date_from_header), '%d %b %Y').strftime('%d.%m.%Y')
    encodings = utils.get_encoding_from_headers(response.headers)
    response = response.content.decode(encoding=encodings)
    response = '_'.join(response.split("<NumCode>"))
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
        currency_dict_all.update({CharCode:
                                      {"NumCode": NumCode,
                                       "Nominal": Nominal,
                                       "Name": Name,
                                       "Value": Value,
                                       "Date": date_from_header
                                       }
                                  })
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
    print(f'Курс валюты {currency_input.upper()} ({currency_dict["Name"]}) на дату {currency_dict["Date"]} = {currency_dict["Value"]}')
