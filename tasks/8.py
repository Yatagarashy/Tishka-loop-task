# В ячейку во второй строке и нулевой колонке записать 4.
import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

matrix[2][0] = 4

print(numpy.array(matrix))