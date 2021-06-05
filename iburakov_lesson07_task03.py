# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации

import os
import shutil

root_dir = 'my_project_2'
for root, dirs, files in os.walk(root_dir):
    if root.split('\\')[-1] == 'templates':
        for name_dir in dirs:
            if name_dir:  # для вложенных папок в templates
                root_path = os.path.join(root, name_dir)
                template_path = os.path.join('my_project_2', 'Templates', name_dir)
                files = [file for file in os.listdir(root_path)
                         if not os.path.isdir(os.path.join(root_path, file))]
                if not os.path.exists(template_path):
                    os.makedirs(template_path)
                for file in files:
                    shutil.copyfile(os.path.join(root_path, file), os.path.join(template_path, file))
