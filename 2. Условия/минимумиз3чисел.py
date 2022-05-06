# Условие: Даны три целых числа. Выведите значение наименьшего из них.
# Решение: 
a = int(input())
b = int(input())
c = int(input())
if a<b and a<c:
    print(a)
elif c<a and c<b:
    print(c)
else: 
    print(b)
