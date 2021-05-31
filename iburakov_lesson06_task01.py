# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

line_out = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = ';'.join(line.split('"'))
        line = ';'.join(line.split(' '))
        line = line.split(';')
        line_out.append((line[0], line[6], line[7]))

with open('nginx_logs_out.txt', 'w', encoding='utf-8') as f:
    for line in line_out:
        f.write(f"{', '.join(line)}\n")
