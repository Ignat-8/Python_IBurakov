# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os
import random

folder = 'some_data'
# ---------------------------------------------------------------------------------
if not os.path.exists(folder):  # формируем 100 файлов разного размера для примера
    os.makedirs(folder)
    letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    for _ in range(10 ** 2):
        f_name = ''.join(random.sample(letters, random.randint(5, 10)))
        f_content = bytes(random.randint(0, 255) for _ in range(random.randrange(10 ** 5)))
        with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
            f.write(f_content)
# ---------------------------------------------------------------------------------
file_stats = {}
for root, dirs, files in os.walk(folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.stat(file_path).st_size
        num = 10 ** len(str(file_size))
        file_stats.setdefault(num, 0)
        file_stats[num] += 1

print(file_stats)
