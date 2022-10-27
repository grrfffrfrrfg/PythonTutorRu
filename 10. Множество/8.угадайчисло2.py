# Условие: Август и Беатриса продолжают играть в игру, но Август начал жульничать. На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO, чтобы множество возможных задуманных чисел оставалось как можно больше. Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то Август ответит NO, а если Беатриса спросит про 1, 2, 3, то Август ответит YES.
# Решение: 
n = int(input())
all_nums = set(range(1,n+1))

while True:
    possible = input()
    if possible == 'HELP':
        break
    possible = set(int(x) for x in possible.split())
    if len(all_nums & possible) > len(all_nums) / 2:
        print('YES')
        all_nums &= possible
    else:
        print('NO')
        all_nums &= all_nums - possible
        
print(*all_nums)
