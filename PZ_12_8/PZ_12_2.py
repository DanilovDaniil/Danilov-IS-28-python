# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def uppercase(s):
    for i in s:
        if isinstance(i, str) and i.isalpha():  # Проверяем, что символ — буква
            yield i.upper()
        else:
            yield i  # Не буквы возвращаются без изменений


s = ['a', 'b', 1, 'c', 'd', 2, 'e', 'f']
e = list(uppercase(s))

print("Преобразованная последовательность:", e)
