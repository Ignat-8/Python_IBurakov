# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении
# данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код,
# загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить
# словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с
# ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что
# объём данных в файлах во много раз меньше объема ОЗУ. Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import sys
import json

f_users = open('users.csv', 'r', encoding='utf-8')
f_hobby = open('hobby.csv', 'r', encoding='utf-8')
f_users_dict = open('users_dict.csv', 'w', encoding='utf-8')
exit_code = 0
users = {}
for line_user in f_users:
    line_hobby = f_hobby.readline()
    if line_hobby == '':
        line_hobby = None
    else:
        line_hobby = line_hobby.strip()
    users.setdefault(line_user.strip().replace(',', ' '), line_hobby)

print(f'сформированный словарь для записи в файл:\n{users}')
json.dump(users, f_users_dict)
if f_hobby.readline() != '':
    exit_code = 1
# -------------------------------------------------------------------
f_users_dict.close()
f_hobby.close()
f_users.close()

# проверяем записанный словарь
f_users_dict = open('users_dict.csv', 'r', encoding='utf-8')
print(f'\nСчитанный словарь из файла:\n{json.load(f_users_dict)}')
f_users_dict.close()

if exit_code == 1:
    sys.exit(1)
