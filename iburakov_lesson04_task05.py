import sys
import utils

if len(sys.argv) == 1:
    currency_input = ''
    while currency_input != 'q':
        currency_input = input('Введите сокращенное название валюты или q для выхода: ')
        currency_dict = utils.currency_rates(currency_input.upper())
        print(f'Курс валюты {currency_input.upper()} ({currency_dict["Name"]}) на дату {currency_dict["Date"]} = {currency_dict["Value"]}')
else:
    currency_input = sys.argv[1]
    currency_dict = utils.currency_rates(currency_input.upper())
    print(f'Курс валюты {currency_input.upper()} ({currency_dict["Name"]}) на дату {currency_dict["Date"]} = {currency_dict["Value"]}')
