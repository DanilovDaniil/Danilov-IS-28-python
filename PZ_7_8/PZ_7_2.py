# Дана строка-предложение с избыточными пробелами между словами.
# Преобразовать ее так, чтобы между словами был ровно один пробел.


try:
    def space(s):
        d = s.split()
        space_ = ' '.join(d)
        return space_
    F = input('Введите предложение с избыточными пробелами: ')
    Z = space(F)
    print(Z)
except ValueError:
    print('Error')
