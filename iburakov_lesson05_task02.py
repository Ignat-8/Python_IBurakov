import random


def odd_nums(max_num):
    """НЕ используя ключевое слово yield"""
    return (random.randrange(1, max_num+1, 2) for _ in range(0, max_num))


print('odd_nums(15):\n', *odd_nums(15))
print('\nodd_nums(21):\n', *odd_nums(21))
