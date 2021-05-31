# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.


def sort_dict_by_value(dict_in, rev=False):
    """
    Осуществляет сортировку словаря по значению ключа
    :param rev:Порядок сортировки. False - по возрастанию, True - по убыванию
    :param dict_in:Входной словарь из пары val: key
    :return:Отсортированный словарь по key
    """
    dict_tmp = dict(sorted({val: key for key, val in dict_in.items()}.items(), reverse=rev))
    return {val: key for key, val in dict_tmp.items()}


def translate_dict_to_list(dict_in):
    """
    Преобразует словарь в список
    :param dict_in:Входной словарь
    :return:Список пар (key, val) из входного словаря
    """
    list_out = []
    for el in dict_in.items():
        list_out.append(el)
    return list_out


# ---------------------------------------------------------------
user_attempts = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(' ')
        user_attempts.setdefault(line[0], 0)
        user_attempts[line[0]] += 1
# ---------------------------------------------------------------
user_attempts = sort_dict_by_value(user_attempts, True)
user_attempts = translate_dict_to_list(user_attempts)
print(f'ip адрес первого спамера {user_attempts[0][0]} с количеством попыток {user_attempts[0][1]}')
print(f'ip адрес второго спамера {user_attempts[1][0]} с количеством попыток {user_attempts[1][1]}')
