# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Новый список не создавать! Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

message_temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message_out = []
for idx, elem in enumerate(message_temp):
    if elem[-1].isdigit():  # для числовых данных проверям
        # дополнение нулем до двух разрядов
        if len(elem) == 1:  # если число из одного разряда
            elem = ''.join(['0', elem])  # то просто добавляем ноль в начале
        elif elem[0] == '+' or elem[0] == '-':  # если в начале числа есть знак + или -
            elem = ''.join([elem[0], '0', elem[1]])  # добавляем 0 в промежутке
        # получившееся число добавляем в выходной список
        message_out.append('"')
        message_out.append(elem)
        message_out.append('"')
    else:  # не числовые данные просто добавляем в выходной список
        message_out.append(elem)
# ----------------------------------------
print('Обработанный список :')
print(message_out)
print()
print(' '.join(['Получилась строка : ', * message_out]))
print(' '.join(['Правильный ответ : ', 'в "05" часов "17" минут температура воздуха была "+05" градусов']))
