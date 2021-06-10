# Реализуйте базовый класс Car. У класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также
# методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car go')
        return 'Car go'

    def stop(self):
        print('Car stop')
        return 'Car stop'

    def turn(self, direction):
        print(f'Car turn {direction}')
        return f'Car turn to {direction}'

    def show_speed(self):
        print(f'Car speed {self.speed}')
        return f'Car speed {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.car_type = 'PoliceCar'
        self.is_police = True


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.car_type = 'SportCar'
        self.is_police = False


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.car_type = 'TownCar'
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} - превышение скорости TownCar!')
            return f'{self.speed} - превышение скорости TownCar!'
        else:
            print(f'TownCar speed {self.speed}')
            return f'TownCar speed {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.car_type = 'WorkCar'
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} - превышение скорости WorkCar!')
            return f'{self.speed} - превышение скорости WorkCar!'
        else:
            print(f'WorkCar speed {self.speed}')
            return f'WorkCar speed {self.speed}'


Car_1 = WorkCar(45, 'blue', 'Mers')
print('Car type - ', Car_1.car_type)
Car_1.show_speed()
Car_1.go()
Car_1.turn('right')
Car_1.stop()
print('color - ', Car_1.color)
print('speed', Car_1.speed)
print('is police - ', Car_1.is_police)
print('-----------------------------------------------------')
Car_2 = TownCar(65, 'blue', 'Mers')
print('Car type - ', Car_2.car_type)
Car_2.show_speed()
print('is police - ', Car_2.is_police)
print('-----------------------------------------------------')
Car_3 = WorkCar(35, 'blue', 'Mers')
print('Car type - ', Car_3.car_type)
Car_3.show_speed()
print('is police - ', Car_3.is_police)
print('-----------------------------------------------------')
Car_4 = PoliceCar(75, 'blue', 'Mers')
print('Car type - ', Car_4.car_type)
Car_4.show_speed()
print('is police - ', Car_4.is_police)
print('-----------------------------------------------------')
