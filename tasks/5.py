# Заполнить от середины списка до конца числами единицами.  
# Первая половина остается нулями.
# То есть [0,0,0,1,1,1]

import math

n = int(input('n='))
d = [0 for _ in range(n)]

d[len(d)//2:len(d)] = [1 for _ in range(math.ceil(len(d)/2))]

print(d)