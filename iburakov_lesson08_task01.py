# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ...
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(email_address):
    re_name = re.compile(r'(?P<username>^[a-zA-Z][A-Za-z0-9-_]+)@(?P<domain>[A-Za-z][A-Za-z0-9-]+([.][A-Za-z0-9-]+){1,3}$)')
    try:
        if re_name.match(email_address):
            email_dict = [elem for elem in map(lambda x: x.groupdict(), re_name.finditer(email_address))]
            return email_dict[0]
        else:
            msg = f'ValueError: wrong email: {email_address}'
            raise ValueError(msg)
    except ValueError as e:
        print(e)
        exit(1)


email_address = 'iburakov-08@ya.sdsdf-2.ru'
print(email_parse(email_address))
