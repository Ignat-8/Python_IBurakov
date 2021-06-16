# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать
# перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_matrix = ''
        for row in self.matrix:
            for el in row:
                str_matrix += f'{el} '
            str_matrix = str_matrix[:-1] + '\n'
        return str_matrix

    def __add__(self, other):
        try:
            if len(self.matrix) == len(other) and len(self.matrix[0]) == len(other[0]):
                out_matrix = []
                for y in range(len(self.matrix)):
                    _ = []
                    for x in range(len(self.matrix[0])):
                        _.append(self.matrix[y][x] + other[y][x])
                    out_matrix.append(_)

                return out_matrix
            else:
                raise ValueError
        except ValueError:
            return f'Error: Матрицы должны быть одинакового размера'

    def __len__(self):
        s = 0
        for _ in self.matrix:
            s += 1
        return s

    def __getitem__(self, item):
        return self.matrix[item]


M_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
M_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Matrix_1 = Matrix(M_1)
Matrix_2 = Matrix(M_2)
print(f'Первая матрица\n{Matrix_1}')
print(f'Вторая матрица\n{Matrix_2}')
print(f'Сумма матриц\n{Matrix(Matrix_1 + Matrix_2)}')
