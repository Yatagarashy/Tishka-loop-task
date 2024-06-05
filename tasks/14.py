# Заполнить матрицу числами по порядку, 
# но направление строк чередуется. 
# Первая слева направо, вторая справаналево, 
# третья слева напрво и т.д.. Результат типа
# [
#     [0,1,2,3],
#     [7,6,5,4],
#     [8,9,10,11],
#     [15,14,13,12],
# ]

import numpy

matrix = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

for row_index, row in enumerate(matrix):
    if row_index % 2 == 0:
        matrix[row_index] = [i for i in range(0+len(row)*row_index, len(row)+len(row)*row_index)]
    else:
        matrix[row_index] = list(reversed([i for i in range(0+len(row)*row_index, len(row)+len(row)*row_index)]))

print(numpy.array(matrix))