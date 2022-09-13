# Условие: Дано действительное положительное число a и целоe число n. Вычислите an. Решение оформите в виде функции power(a, n).
# Решение:
# Способ 1:
a = float(input())
n = int(input())
def power(a, n):
    p = a**n
    return(p)
print(power(a, n))
