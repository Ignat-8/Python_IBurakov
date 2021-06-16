# Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта и
# проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.V = size

    @property
    def fabric_consumption(self):
        return f'{self.V / 6.5 + 0.5:0.2} м2'


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.H = height

    @property
    def fabric_consumption(self):
        return f'{self.H * 2 + 0.3} м2'


Costume_1 = Costume('Costume_1', 172)
print(Costume_1.fabric_consumption)

Coat_1 = Coat('Coat_1', 48)
print(Coat_1.fabric_consumption)
