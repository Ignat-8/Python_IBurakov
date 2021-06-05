# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при
# этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os
import json

folder_struct = {}
with open('my_project_folders.txt', 'r', encoding='utf-8') as f_folders_struct:
    folder_struct = json.load(f_folders_struct)  # загрузили словарь со структурой папок

new_folders = [folder_struct[folder].get('folder_name') for folder in folder_struct]
for folder in new_folders:
    dir_path = os.path.join('my_project', folder)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
