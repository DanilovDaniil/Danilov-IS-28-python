# В двумерном списке элементы столбца N (N задать с клавиатуры) увеличить в два
# раза.


r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))

matrix = list(map(lambda i: list(map(int, input(f"Введите {c} элементов строки {i+1} через пробел: ").split())),
                  range(r)))

N = int(input("Введите номер столбца N начиная с 0: "))

index = list(range(c))

result = list(map(lambda r: list(map(lambda c: r[c] * 2 if c == N else r[c], index)), matrix))

print("Результат:")
for i in result:
    print(i)
