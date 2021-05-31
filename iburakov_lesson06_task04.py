# Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально
# создавать такие большие файлы, это просто задел на будущее проекта). Также реализовать парсинг данных из файлов -
# получить отдельно фамилию, имя и отчество для пользователей и название каждого хобби: преобразовать в какой-нибудь
# контейнерный тип (список, кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут возникнуть
# проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.

import sys
import json

f_users = open('users.csv', 'r', encoding='utf-8')
f_hobby = open('hobby.csv', 'r', encoding='utf-8')
f_users_dict = open('users_dict2.csv', 'w', encoding='utf-8')
exit_code = 0
users = {}
for line_user in f_users:
    line_hobby = f_hobby.readline()
    if line_hobby == '':
        line_hobby = None
    else:
        line_hobby = line_hobby.strip().split(',')
    user_list = line_user.split(',')
    user_surname = user_list[0].strip(' ')
    user_name = user_list[1].strip(' ')
    user_patronymic = user_list[2].strip(' ').strip()
    users.setdefault(line_user.strip().replace(',', ' '), {
        'Surname': user_surname,
        'Name': user_name,
        'Patronymic': user_patronymic,
        'Hobby': line_hobby
    })

print(f'сформированный словарь для записи в файл:\n{users}')
json.dump(users, f_users_dict)
if f_hobby.readline() != '':
    exit_code = 1
# -------------------------------------------------------------------
f_users_dict.close()
f_hobby.close()
f_users.close()

# проверяем записанный словарь
f_users_dict = open('users_dict2.csv', 'r', encoding='utf-8')
print(f'\nСчитанный словарь из файла:\n{json.load(f_users_dict)}')
f_users_dict.close()

if exit_code == 1:
    sys.exit(1)
