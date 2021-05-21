# Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.


def num_translate(world):
    """ Перевод русских и английских числительных """
    enumerate_dict = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'один': 'one',
        'два': 'two',
        'три': 'three',
        'четыре': 'four',
        'пять': 'five',
        'шесть': 'six',
        'семь': 'seven',
        'восемь': 'eight',
        'девять': 'nine',
        'десять': 'ten'
        }
    if enumerate_dict.get(world):
        return f'Перевод {world} - {enumerate_dict.get(world)}'
    else:
        return None


world_translate = input('Введите числительное для перевода на русский\английский или q для выхода: ')
while world_translate != 'q':
    print(num_translate(world_translate))
    world_translate = input('Введите числительное для перевода на русский\английский или q для выхода: ')
