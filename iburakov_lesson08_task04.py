# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

from functools import wraps


def val_checker(cond):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            try:
                if cond(*args):
                    return func(*args)
                else:
                    msg = f'ValueError: wrong value: {args[0]} in function {func.__name__}()'
                    raise ValueError(msg)
            except ValueError as e:
                print(e)
                exit(1)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(-5))
