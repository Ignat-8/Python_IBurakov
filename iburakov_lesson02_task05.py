# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). 
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

import random

price_list = []
message_out = ''
for _ in range(1, 20):
    price = round(random.random() * 100, 2)
    price_list.append(price)
    price = str(price).split('.')
    price[1] = "{:02d}".format(int(price[1]))
    message_out += ' '.join([price[0], 'руб', price[1], 'коп']) + ', '
# -------------------------------------------------------------
print('Список цен:')
print(message_out)
print()
print('id(price_list) = ' + str(id(price_list)))
print()
print('Отсортированный список цен:')
price_list.sort()
message_out = ''
for _ in range(0, 19):
    price = price_list[_]
    price = str(price).split('.')
    price[1] = "{:02d}".format(int(price[1]))
    message_out += ' '.join([price[0], 'руб', price[1], 'коп']) + ', '

print(message_out)
print()
print('id(price_list_sorted) = ' + str(id(price_list)))

# -------------------------------------------------------------
print('Список цен по убыванию : ')
price_list2 = price_list.copy()
price_list2.sort(reverse = True)

message_out = ''
for _ in range(0, 19):
    price = price_list2[_]
    price = str(price).split('.')
    price[1] = "{:02d}".format(int(price[1]))
    message_out += ' '.join([price[0], 'руб', price[1], 'коп']) + ', '
print(message_out)
print()

# ----------------------------------------------------------
print('Цены 5-ти самых дорогих товаров')
price_list_top5 = price_list[-5:]

message_out = ''
for _ in range(0, 4):
    price = price_list_top5[_]
    price = str(price).split('.')
    price[1] = "{:02d}".format(int(price[1]))
    message_out += ' '.join([price[0], 'руб', price[1], 'коп']) + ', '
print(message_out)
print()



