# Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания. Создать скрипт,
# в котором импортировать этот модуль и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
# лишнего не происходит.

import utils

currency_input = ''
while currency_input != 'q':
    currency_input = input('Введите сокращенное название валюты или q для выхода: ')
    currency_dict = utils.currency_rates(currency_input.upper())
    print(f'Курс валюты {currency_input.upper()} ({currency_dict["Name"]}) на дату {currency_dict["Date"]} = {currency_dict["Value"]}')
