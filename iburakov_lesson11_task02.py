# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

import traceback


class Own_Exception(Exception):
    @staticmethod
    def check_division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return f'Ошибка:\n{traceback.format_exc()}'


print(Own_Exception.check_division(5, 0))
