# Заполнить матрицу по спирали
# Вот так:

#  1  2  3  4
# 12 13 14  5
# 11 16 15  6
# 10  9  8  7

import numpy

n = int(input('n='))
matrix = [[None for _ in range(n)] for _ in range(n)]


x, y = 0, 0
run_x = 1
run_y = 0

for i in range(n**2):
    if x <= n-1 and x >= 0 and y <= n-1 and y >= 0 and matrix[y][x] is None:
        matrix[y][x] = i
    else:
        x-=run_x
        y-=run_y
        if run_x == 1:
            run_x = 0
            run_y = 1
        elif run_y == 1:
            run_x = -1
            run_y = 0
        elif run_x == -1:
            run_x = 0
            run_y = -1
        elif run_y == -1:
            run_x = 1
            run_y = 0
        x+=run_x
        y+=run_y
        matrix[y][x] = i
    
    x+=run_x
    y+=run_y

print(numpy.array(matrix))