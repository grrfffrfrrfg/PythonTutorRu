# Условие:Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
# Решение: 
countString = int(input())
words = set() 

for i in range(countString):
    for x in input().split():
        words.add(x)
        
print(len(words))


