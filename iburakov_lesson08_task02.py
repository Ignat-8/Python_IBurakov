# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt для получения
# информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP
# /1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as f_in, \
        open('nginx_logs_out.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('remote_addr, request_datetime, request_type, requested_resource, response_code, response_size\n')
    for line in f_in:
        re_name = re.compile(r'(^[0-9.:a-z]+)\s-\s-\s\[(.+)\]\s\"([A-Z]+)\s([a-zA-Z0-9/_.\ ]+)\"\ (\d+)\ (\d+)\ ')
        parsed_raw = re_name.findall(line)[0]
        f_out.write(f"{', '.join(parsed_raw)}\n")
