# Составить программу, в которой функцию построит изображение, в котором в
# первой строке 1 звездочка, во второй - 2, в третьей -3, ..., в строке с номером m - m
# звездочек.

try:
    def stars(m):
        for i in range(1, m + 1):
            print('*' * i)
    m_ = int(input("Ведите количество строк: "))
    stars(m_)
except ValueError:
    print("Ошибка")
