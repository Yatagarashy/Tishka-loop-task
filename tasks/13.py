# Заполнить матрицу числа по порядку: сначала нулевую строку, 
# потому первую и т.п. 
# Должно получиться что-то типа [[0,1,2],[3,4,5],[6,7,8]]

import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]

for row_index, row in enumerate(matrix):
    matrix[row_index] = [i for i in range(0+len(row)*row_index, len(row)+len(row)*row_index)]


print(numpy.array(matrix))