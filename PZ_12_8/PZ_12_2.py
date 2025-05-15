# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def uppercase(s):
    for i in s:
        if isinstance(i, str) and i.isalpha():
            yield i.upper()
        else:
            yield i


s = ['a', 'b', 1, 'c', 'd', 2, 'e', 'f']
e = list(uppercase(s))
print("Преобразованная последовательность:", e)
