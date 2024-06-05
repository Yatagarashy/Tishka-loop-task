# Заполнить нулевую строку матрицы единицами

import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]


matrix[0] = [1 for _ in range(len(matrix[0]))]

print(numpy.array(matrix))