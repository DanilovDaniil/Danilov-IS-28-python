# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.


def double_column(matrix, column):
    for i in matrix:
        if column < len(i):
            i[column] *= 2


d = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(d):
    b = list(map(int, input(f"Введите {cols} элементов строки {i+1}: ")))
    matrix.append(b)

N = int(input("Введите номер столбца N начиная с 0: "))

double_column(matrix, N)

print("Результат:")
for b in matrix:
    print(b)

