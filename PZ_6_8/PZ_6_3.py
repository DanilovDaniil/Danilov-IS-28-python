# Дан список размера N. Заменить каждый элемент списка на среднее арифметическое
# этого элемента и его соседей.

try:
    s = [-1, 0.4, 84, 2.5, 396]

    def srd_arfm(n):
        d = len(n)
        b = []
        for i in range(d):
            if i == 0:
                v = (n[i] + n[i + 1]) / 2
            elif i == d - 1:
                v = (n[i - 1] + n[i]) / 2
            else:
                v = (n[i - 1] + n[i] + n[i + 1]) / 3
            b.append(v)
        return b
    g = srd_arfm(s)
    print(g)
except ValueError:
    print("Ошибка")
