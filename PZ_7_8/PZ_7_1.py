# Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
# символов C.
try:
    N = int(input('Введите целое число которое больше 0: '))
    C = input('Введите символ: ')
    if N > 0:
        print(N * C)
    else:
        print('Ошибка')
except ValueError:
    print("Error")
