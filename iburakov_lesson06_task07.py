# Добавить возможность редактирования данных при помощи отдельного скрипта: передаём ему номер записи и новое значение.
# При этом файл не должен читаться целиком — обязательное требование. Предусмотреть ситуацию, когда пользователь вводит
# номер записи, которой не существует.

# Этот скрипт редактирует данные в файле bakery_sales.csv
import sys


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False


if len(sys.argv) == 1:  # без аргументов просто выводим список
    with open('bakery_sales.csv', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(f'{float(line.strip())}')
            line = f.readline()

if len(sys.argv) == 2:
    print(f'Введите два числа - номер записи и новую сумму продаж')

if len(sys.argv) == 3:
    sum_sales = sys.argv[2].replace(',', '.')
    if sys.argv[1].isdigit() and is_float(sum_sales):  # если оба значения числа
        with open('bakery_sales.csv', 'r+', encoding='utf-8') as f:
            sum_sales = f'{float(sum_sales):09.2f}'  # делаем все числа одного формата и длины для поиска в файле
            f.seek(0, 2)  # перемещаемся в конец файла
            if f.tell() > (int(sys.argv[1]) - 1) * 11:
                f.seek((int(sys.argv[1]) - 1) * 11, 0)
                f.write(sum_sales)
                print(f'Запись с номером {sys.argv[1]} обновлена значением {float(sum_sales)}')
            else:
                print(f'Записи с номером {sys.argv[1]} нет')
    else:
        print(f'Введите два числа - номер записи и новую сумму продаж')
