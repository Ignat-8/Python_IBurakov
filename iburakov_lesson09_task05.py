# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
# переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
        self.message = ''

    def drow(self):
        self.message = 'Запуск отрисовки класса Stationery'
        print(self.message)
        return self.message


class Pen(Stationery):
    def drow(self):
        self.message = f'Запуск отрисовки класса Pen'
        print(self.message)
        return self.message


class Pencil(Stationery):
    def drow(self):
        self.message = f'Запуск отрисовки класса Pencil'
        print(self.message)
        return self.message


class Handle(Stationery):
    def drow(self):
        self.message = f'Запуск отрисовки класса Handle'
        print(self.message)
        return self.message


Stationery_1 = Stationery('Stationery_1')
Stationery_1.drow()

Pen_1 = Pen('Pen_1')
Pen_1.drow()

Pencil_1 = Pencil('Pencil_1')
Pencil_1.drow()

Handle_1 = Handle('Handle_1')
Handle_1.drow()
