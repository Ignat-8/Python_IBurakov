import random


def odd_nums(max_num):
    """Используя слово ключевое yield"""
    for num in range(0, max_num):
        yield random.randrange(1, max_num+1, 2)


odd_to_15 = odd_nums(15)
print('odd_nums(15):\n', *odd_to_15)

print('odd_nums(15):\n', *odd_nums(21))
