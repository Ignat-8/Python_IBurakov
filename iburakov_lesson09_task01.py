# Создать класс TrafficLight (светофор). Определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный. Продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from time import perf_counter


class TrafficLight:
    def __init__(self):
        self.__color = 'красный'

    def running(self):
        if self.__color == 'красный':
            start_time = perf_counter()
            while perf_counter() - start_time < 7:
                pass
            self.__color = 'желтый'
            return self.__color
        if self.__color == 'желтый':
            start_time = perf_counter()
            while perf_counter() - start_time < 2:
                pass
            self.__color = 'зеленый'
            return self.__color
        if self.__color == 'зеленый':
            start_time = perf_counter()
            while perf_counter() - start_time < 5:
                pass
            self.__color = 'красный'
            return self.__color


TrafficLight_1 = TrafficLight()
print('Первоначальный цвет сфетофора ', TrafficLight_1._TrafficLight__color, ', время старта 0 сек')

start_time = perf_counter()
TrafficLight_1.running()
print('Первое переключение сфетофора ', TrafficLight_1._TrafficLight__color, ', время работы ', perf_counter() - start_time)

start_time = perf_counter()
TrafficLight_1.running()
print('Второе переключение сфетофора ', TrafficLight_1._TrafficLight__color, ', время работы ', perf_counter() - start_time)

start_time = perf_counter()
TrafficLight_1.running()
print('Третье переключение сфетофора ', TrafficLight_1._TrafficLight__color, ', время работы ', perf_counter() - start_time)
