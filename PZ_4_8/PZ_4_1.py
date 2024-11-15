# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
# до B включительно.
try:
    a = int(input('Введите число "a" '))
    b = int(input('Введите число "b" '))
    if a < b:
        c = sum(i**2 for i in range(a, b + 1))
        print("Сумма квадратов целых чисел", c)
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")
