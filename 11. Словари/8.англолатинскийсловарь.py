# Условие:  см тут -> https://pythontutor.ru/lessons/dicts/problems/english_latin_dict/
# Решение:
l = []
wordE = {}
wordL = {}

for i in range(int(input())):
    l = input().split()
    wordE[l[0]] = l[2:]
    
for k, v in wordE.items(): # цикл, бегающий по каждому элементу
    for i in v: # в цикле мы получаем ключ и каждое его значение(т.е key and value)
        if wordL.get(i.replace(',',''), 0) != 0: # внутри цикла мы перебираем слова 
            wordL[i.replace(',','')] += ', ' + k # и заменяем методом replace символ ',' на пустой символ
        else:
            wordL[i.replace('','')] = k
            
print(len(wordL)) # принтуем сколько строк у нас получилось
 
for k, v in sorted(wordL.items()): # вызываем функцию, которая добавляет тире и значение слова на английском 
    print(k.replace(',',''), '-', v)
