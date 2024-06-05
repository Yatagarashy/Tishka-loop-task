# Завести переменные x=1, y=2 и завести с ячеку в строке y и колонке x записать -1

import numpy

matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
x = 1
y = 2

matrix[y][x] = -1

print(numpy.array(matrix))