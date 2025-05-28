# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.

def up(s):
    for i in s:
        yield i.swapcase()


t = "d f g h n"
g = up(t)

for i in g:
    print(i)
