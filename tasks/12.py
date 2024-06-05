# Заполнить нулевой столбец матрицы числами по порядку 0,1,2...

import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

for index, row in enumerate(matrix):
    row[0] = index


print(numpy.array(matrix))