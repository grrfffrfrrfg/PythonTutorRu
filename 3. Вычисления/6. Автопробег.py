# Условие: За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? Программа получает на вход числа n и m.
# Решение:
n = int(input())
m = int(input())
print((m + n - 1) // n)
# можно было через библиотеку math: 
# print(ceil(m / n))
