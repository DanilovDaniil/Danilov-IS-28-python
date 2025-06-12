# В двумерном списке элементы последней строки заменить на 0.

import random

r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

matrix = [[random.randint(1, 100) for i in range(c)] for j in range(r)]

print("\nСгенерированная матрица:")
for i in matrix:
    print(i)

result = list(map(lambda i: [0] * c if i == r - 1 else matrix[i], range(r)))

print("Результат:")
for i in result:
    print(i)

