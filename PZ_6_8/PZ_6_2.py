# Дан список размера N. Найти количество участков, на которых его элементы
# монотонно возрастают.

try:
    n = [-1, -3, 4, -10, 3, -2, 4, 5, -45]

    def vsrst(n):
        v = 0
        s = 1
        for i in range(1, len(n)):
            if n[i] > n[i - 1]:
                s += 1
            else:
                if s > 1:
                    v = 1
        if s > 1:
            v += 1
        return v
    vsrst(n)
    print("Количество участков элементы которых возрастают: ", vsrst(n))
except ValueError:
    print("Ошибка")
