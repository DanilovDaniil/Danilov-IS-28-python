# Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A
# до B включительно.
try:
    a = int(input('Введите число "a" '))
    b = int(input('Введите число "b" '))
    if a <= b:
        print("Сумма квадратов целых чисел", a * a + b * b)
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")