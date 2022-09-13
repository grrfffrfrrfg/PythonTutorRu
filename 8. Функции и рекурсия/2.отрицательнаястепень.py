# Условие: Дано действительное положительное число a и целоe число n. Вычислите an. Решение оформите в виде функции power(a, n).
# Решение:
# Способ 1:
a = float(input())
n = int(input())
def power(a, n):
    p = a**n
    return(p)
print(power(a, n))
# Второй способ
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a 
    if n<0:
        return 1/res
    else:
        return res
    
    
a = float(input())
n = int(input())

print(power(a, n))
