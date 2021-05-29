import random


def odd_nums(max_num):
    """Используя ключевое слово yield"""
    for num in range(0, max_num):
        yield random.randrange(1, max_num+1, 2)


print('odd_nums(15):\n', *odd_nums(15))
print('\nodd_nums(21):\n', *odd_nums(21))
