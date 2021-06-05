# Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

import os
import json

folder_struct = {}
with open('config.yaml', 'r', encoding='utf-8') as f_folders_struct:
    folder_struct = json.load(f_folders_struct)  # загрузили словарь со структурой папок

for _ in folder_struct:
    dir_path = os.path.join('my_project_2', folder_struct[_]['folder_name'])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for file in folder_struct[_]['files_name'].split(','):
        if file:
            file_path = os.path.join(dir_path, file.strip(' '))
            with open(file_path, 'w', encoding='utf-8') as f:
                pass
