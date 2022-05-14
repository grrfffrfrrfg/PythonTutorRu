# Условие: Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).
# Решение: 
plot = input().split()
for i in range(len(plot)):
    if i%2==0:
        print(plot[i])
