# 1. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное».

a = int(input("Введите первое число:"))
b = int(input("Введите второе число: "))

a1 = (a % 2) == 1
b1 = (b % 2) == 1
x = a1 and b1
print("a нечётное: ", a1)
print("b нечётное: ", b1)
print("a и b нечётны: ", x)
