# Решение: Даны два элемента в дереве. Определите, является ли один из них потомком другого.
# Условие:
d = {}
for _ in range(int(input()) - 1):
    pot, predok = map(str, input().split())
    d[pot] = predok
for _ in range(int(input())):
    hum1, hum2 = map(str, input().split())
    p1, p2 = hum1, hum2
    s = 2
    while s != 0:
        if p1 in d:
            if d[p1] == hum2:
                break
            else:
                p1 = d[p1]
        else:
            hum1, hum2 = hum2, hum1
            p1, p2 = hum1, hum2
            s -= 1
    print(s, end=' ')
