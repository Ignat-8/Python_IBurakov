# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
# подходящую структуру (например, словарь).
# Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, отправленных
# на склад, нельзя использовать строковый тип данных.

class Warehouse:
    warehouse_table = {'warehouse': {}, 'offices': {}}

    @classmethod
    def to_recept(cls, cnt):
        if Warehouse.check_number(cnt):
            if cls.warehouse_table['warehouse'].get(cls.equipment_type):
                cls.warehouse_table['warehouse'][cls.equipment_type] += cnt
            else:
                cls.warehouse_table['warehouse'].setdefault(cls.equipment_type, cnt)

            return cls.warehouse_table
        else:
            print(f"Вместо числа Вы ввели строку '{cnt}' для оборудования {cls.equipment_type}. Эти данные не будут добавлены\n")
            return False

    @classmethod
    def to_take(cls, cnt, office_name):
        cls.warehouse_table['warehouse'][cls.equipment_type] -= cnt
        if cls.warehouse_table['offices'].get(office_name):
            if cls.warehouse_table['offices'][office_name].get(cls.equipment_type):
                cls.warehouse_table['offices'][office_name][cls.equipment_type] += cnt
            else:
                cls.warehouse_table['offices'][office_name].setdefault(cls.equipment_type, cnt)
        else:
            cls.warehouse_table['offices'].setdefault(office_name, {cls.equipment_type: cnt})

    @staticmethod
    def check_number(number):

        try:
            int(number)
            if isinstance(number, str):
                raise ValueError
            return True
        except ValueError:
            return False


class Office_Equipment(Warehouse):
    def __init__(self):
        Office_Equipment.offices = ['office_1', 'office_2', 'office_3']


class Printer(Office_Equipment):
    def __init__(self):
        super().__init__()
        Printer.equipment_type = 'printer'


class Scanner(Office_Equipment):
    def __init__(self):
        super().__init__()
        Scanner.equipment_type = 'scanner'


class Xerox(Office_Equipment):
    def __init__(self):
        super().__init__()
        Xerox.equipment_type = 'xerox'


# Добавляем на склад принтеры
eq_1 = Printer()
eq_1.to_recept(8)
eq_1.to_recept(2)
eq_1.to_recept('2')

# Добавляем на склад сканеры
eq_2 = Scanner()
eq_2.to_recept(10)

# Добавляем на склад ксероксы
eq_3 = Xerox()
eq_3.to_recept(10)

# выводим начальное состояние склада
print(f'Начальное состояние склада:\n{Warehouse.warehouse_table}')

# передаем оборудование в 1 офис
eq_1.to_take(3, 'office_1')
eq_2.to_take(3, 'office_1')
eq_3.to_take(3, 'office_1')

# передаем оборудование в 2 офис
eq_1.to_take(3, 'office_2')
eq_2.to_take(3, 'office_2')
eq_3.to_take(3, 'office_2')

# передаем оборудование в 3 офис
eq_1.to_take(3, 'office_3')
eq_2.to_take(3, 'office_3')
eq_3.to_take(3, 'office_3')

# выводим конечное состояние склада
print(f'Конечное состояние склада:\n{Warehouse.warehouse_table}')
