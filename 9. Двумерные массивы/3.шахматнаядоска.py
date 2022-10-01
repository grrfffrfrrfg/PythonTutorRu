# Условие: Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка.
# Решение: 
n, m = [int(i) for i in input().split()]
n_1 = []
for i in range(n):
    n_1.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            n_1[i].append('.')
        else:
            n_1[i].append('*')
for row in n_1:
    print(' '.join(row))
            
