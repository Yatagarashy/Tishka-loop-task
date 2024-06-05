# Вывести с помощью цикла for и range квадраты чисел от 0 до n. То есть 0,1,4,...n**2

n = int(input('n='))

for i in range(n):
    print(i**2)

# Выпендрежный вариант
print(" ".join(map(str,[i**2 for i in range(n)])))
