# Условие: В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. Для каждого файла известно, с какими действиями можно к нему обращаться:
# Решение: 
n = int(input())  # сколько всего строк
x = {'write':'W','read':'R','execute':'X'}
d={}

for i in range(n):
    a,*b=input().split()
    d[a]=set(b)

for i in range(int(input())):
    a,b=input().split()
    if x[a] in d[b]:
        print('OK')
    else:
        print('Access denied')
