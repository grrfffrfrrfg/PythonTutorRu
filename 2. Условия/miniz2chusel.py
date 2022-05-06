# Условие: Даны два целых числа. Выведите значение наименьшего из них.
# Решение:
x = int(input())
y = int(input())
if x<y: 
    print(x)
else:
    print(y)

# or print(min(x,y)) - но наши задачи нужно решать через if и else 
