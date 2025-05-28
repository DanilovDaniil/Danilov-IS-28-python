# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.


r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

matrix = list(map(lambda i: list(map(int, input(f"Введите {c} элементов строки {i+1} через пробел: ").split())),
                  range(r)))

N = int(input("Введите номер столбца N начиная с 0: "))

ind = list(range(c))

result = list(map(lambda r: list(map(lambda col_index: r[col_index] * 2 if col_index == N else r[col_index],ind)),
                  matrix))

print("Результат:")
for row in result:
    print(row)
