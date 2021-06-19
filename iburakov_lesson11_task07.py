# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class Complex_number:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img >= 0:
            return f'{self.real} + {self.img}i'
        else:
            return f'{self.real} - {-1 * self.img}i'

    def __add__(self, other):
        if (self.img + other.img) >= 0:
            return f'{self.real + other.real} + {self.img + other.img}i'
        else:
            return f'{self.real + other.real} - {(self.img + other.img) * -1}i'

    def __sub__(self, other):
        if (self.img - other.img) >= 0:
            return f'{self.real - other.real} + {self.img - other.img}i'
        else:
            return f'{self.real - other.real} - {(self.img - other.img) * -1}i'

    def __mul__(self, other):
        if (self.real * other.img + self.img * other.real) >= 0:
            return f'{self.real * other.real - self.img * other.img} + {self.real * other.img + self.img * other.real}i'
        else:
            return f'{self.real * other.real - self.img * other.img} - {(self.real * other.img + self.img * other.real) * -1}i'


a = Complex_number(1, 2)
b = Complex_number(3, 4)
print(f'число a = {a}')
print(f'число b = {b}')
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
