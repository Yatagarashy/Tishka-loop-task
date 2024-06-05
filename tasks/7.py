# Заполнить список от середины числа по порядку начиная с числа start, 
# пока не встретится число кратное 4.
# Остаток списка заполнить числом -1.
# Например, start=7 и d=[0,0,0,0,0,0,0,0] => [0,0,0,0,7,8,-1,-1]

import math

n = int(input('n='))
start = int(input('start='))
d = [0 for _ in range(n)]


stop_flag = False

d[len(d)//2:len(d)] = [i if not (stop_flag := True if i%4==1 else stop_flag) else -1 for i in range(start, math.ceil(len(d)/2)+start)]

print(d)
