# Реализовать базовый класс Worker (работник). Определить атрибуты: name, surname, position (должность), income
# (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}; Cоздать класс Position (должность) на базе класса Worker; В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)

    def get_full_name(self):
        full_name = f'{self.surname} {self.name}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] * (1 + self._income['bonus'] / 100)
        return total_income


income = {'wage': 100, 'bonus': 30}
Position_1 = Position("Igor", "Burakov", "engineer", income)
print('Атрибуты класса Position:')
print('surname = ', Position_1.surname)
print('name = ', Position_1.name)
print('position = ', Position_1.position)
print('income = ', Position_1._income)
print('Методы:')
print('get_full_name() = ', Position_1.get_full_name())
print('get_total_income() = ', Position_1.get_total_income())
