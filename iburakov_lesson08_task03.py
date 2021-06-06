# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете
# ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):  # (5, 7)
        nonlocal cache
        for key in args:
            if key not in cache:
                cache[key] = func(key)
        return cache[key]  # {5: 125, 7: 343}
    return wrapper


def type_logger(func):
    def wrapper(*args):
        result = [f'{func.__name__}({num}: {type(num)})' for num in args]
        return result
    return wrapper


@type_logger
@simple_cache
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 7), sep='\n')
