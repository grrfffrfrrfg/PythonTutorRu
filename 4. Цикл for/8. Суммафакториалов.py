# Условие: По данному натуральном n вычислите сумму 1!+2!+3!+...+n!. В решении этой задачи можно использовать только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.
# Решение: 
n = int(input())
sum_of_factorials = 1
curr_factorial = 1
for i in range(2, n + 1):
    curr_factorial *= i
    sum_of_factorials += curr_factorial
print(sum_of_factorials)
