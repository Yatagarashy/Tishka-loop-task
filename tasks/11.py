# Заполнить нулевую строку матрицы квадратами чисел как в задании 3: 0,1,4...

import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]


matrix[0] = [i**2 for i in range(len(matrix[0]))]

print(numpy.array(matrix))