# Условие:Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
# Решение:
def capitalize(st):
  st = st.split()
  for i in range(len(st)):
    symbol = ord(st[i][0]) - 32
    st = chr(symbol) + st[i][1:]
  st = ' '.join()
  return st


word = input
print(capitalize(st))
