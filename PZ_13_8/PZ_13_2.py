# В двумерном списке элементы последней строки заменить на 0.

r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

matrix = [list(map(int, input(f"Введите {c} элементов строки {i+1} через пробел: ").split())) for i in range(r)]

new_matrix = list(map(lambda i: [0] * c if i == r - 1 else matrix[i], range(r)))

print("Результат:")
for row in new_matrix:
    print(row)

