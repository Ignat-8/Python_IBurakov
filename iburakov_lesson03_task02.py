# * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы.
# Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


def num_translate(world):
    """ Перевод русских и английских числительных """
    enumerate_dict = {
        'One': 'Один',
        'one': 'один',
        'Two': 'Два',
        'two': 'два',
        'Three': 'Три',
        'three': 'три',
        'Four': 'Четыре',
        'four': 'четыре',
        'Five': 'Пять',
        'five': 'пять',
        'Six': 'Шесть',
        'six': 'шесть',
        'Seven': 'Семь',
        'seven': 'семь',
        'Eight': 'Восемь',
        'eight': 'восемь',
        'Nine': 'Девять',
        'nine': 'девять',
        'Ten': 'Десять',
        'ten': 'десять',
        'Один': 'One',
        'один': 'one',
        'Два': 'Two',
        'два': 'two',
        'Три': 'Three',
        'три': 'three',
        'Четыре': 'Four',
        'четыре': 'four',
        'Пять': 'Five',
        'пять': 'five',
        'Шесть': 'Six',
        'шесть': 'six',
        'Семь': 'Seven',
        'семь': 'seven',
        'Восемь': 'Eight',
        'восемь': 'eight',
        'Девять': 'Nine',
        'девять': 'nine',
        'Десять': 'Ten',
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
