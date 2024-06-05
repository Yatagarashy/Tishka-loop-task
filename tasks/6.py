# Заполнить от середины списка до конца числами 1,2,3... 
# Первая половина остается нулями. 
# То есть [0,0,0,1,2,3]

import math

n = int(input('n='))
d = [0 for _ in range(n)]

d[len(d)//2:len(d)] = [i for i in range(1, math.ceil(len(d)/2)+1)]

print(d)