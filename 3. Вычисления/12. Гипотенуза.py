# Условие: Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
# Решение: 
import math
a = int(input())
b = int(input())
x = (a*a)+(b*b)

print(math.sqrt(x))

