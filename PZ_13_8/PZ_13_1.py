# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.


import random

r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

matrix = [[random.randint(1, 100) for i in range(c)] for j in range(r)]

print("\nСгенерированная матрица:")
for i in matrix:
    print(i)

N = int(input("Введите номер столбца N начиная с 0: "))

index = list(range(c))

result = list(map(lambda r: list(map(lambda c: r[c] * 2 if c == N else r[c], index)), matrix))

print("Результат:")
for i in result:
    print(i)
