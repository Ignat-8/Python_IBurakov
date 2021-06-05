# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же, а значения —
# кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import random
import json

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
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        file_stats.setdefault(num, [0])
        file_stats[num][0] += 1
        if ext not in file_stats[num]:
            file_stats[num].append(ext)

for key, val in file_stats.items():  # преобразуем словарь к нужному виду
    file_stats[key] = tuple((val[0], val[1:]))

with open(f'{folder}_summary.json', 'w', encoding='utf-8') as f:
    json.dump(file_stats, f)
