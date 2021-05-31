# Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к обоим исходным файлам и
# путь к выходному файлу со словарём. Проверить работу скрипта для случая, когда все файлы находятся в разных папках.

import sys
import json

if len(sys.argv) == 4:
    url_users = sys.argv[1]
    url_hobby = sys.argv[2]
    url_dict = sys.argv[3]

    if url_users[-1] != '/':
        url_users = url_users + '/'
    if url_hobby[-1] != '/':
        url_hobby = url_hobby + '/'
    if url_dict[-1] != '/':
        url_dict = url_dict + '/'

    f_users = open(f'{url_users}users.csv', 'r', encoding='utf-8')
    f_hobby = open(f'{url_hobby}hobby.csv', 'r', encoding='utf-8')
    f_users_dict = open(f'{url_dict}users_dict2.csv', 'w', encoding='utf-8')

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
    f_users_dict = open(f'{url_dict}users_dict2.csv', 'r', encoding='utf-8')
    print(f'\nСчитанный словарь из файла:\n{json.load(f_users_dict)}')
    f_users_dict.close()

    if exit_code == 1:
        sys.exit(1)
else:
    print(f'Введите путь к файлу users.csv, файлу hobby.csv и выходному файлу users_dict2.csv')
