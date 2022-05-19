# Условие: В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
# Решение: 
n=[int(i) for i in input().split()]
max=n.index(max(n))
min=n.index(min(n))
n[max],n[min] = n[min],n[max]
print(' '.join(str(i) for i in n))
