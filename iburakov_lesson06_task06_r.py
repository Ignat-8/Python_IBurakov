# Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# 1. просто запуск скрипта — выводить все записи;
# 2. запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# 3. запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму
# числу, включительно.

# Этот скрипт для чтения данных из текстового файла продаж
import sys

if len(sys.argv) == 1:
    with open('bakery_sales.csv', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(f'{float(line.strip())}')
            line = f.readline()

if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        pos_start = (int(sys.argv[1]) - 1) * 11
        with open('bakery_sales.csv', 'r', encoding='utf-8') as f:
            f.seek(0, 2)  # перемещаемся в конец файла
            if pos_start < f.tell():  # исключаем возможность выхода за пределы файла
                f.seek(pos_start)
                for line in f:
                    print(f'{float(line.strip())}')
            else:
                print(f'В файле меньше {sys.argv[1]} строк')
    else:
        print(f'Введите номер записи, с которой начать вывод данных')

if len(sys.argv) == 3:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        pos_start = (int(sys.argv[1]) - 1) * 11
        pos_stop = (int(sys.argv[2]) + 1) * 11
        with open('bakery_sales.csv', 'r', encoding='utf-8') as f:
            f.seek(0, 2)  # перемещаемся в конец файла
            if pos_stop > f.tell():  # исключаем возможность выхода за пределы файла
                pos_stop = f.tell()

            f.seek(pos_start)
            for _ in range(pos_start, pos_stop, 11):
                line = f.readline()
                print(f'{float(line.strip())}')
    else:
        print(f'Введите два номера записи, с которых начать вывод данных')
