# Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в словари, с использованием функции найти среднее значение продаж по
# каждому виду продукции, результаты вывести на экран.

s = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'


def srzn(s):
    parts = s.split()
    v = {}
    tek_product = None
    for part in parts:
        if part.isdigit():
            if tek_product:
                v[tek_product].append(int(part))
        else:
            tek_product = part
            v[tek_product] = []
    resh = {tek_product: sum(values) / len(values) for tek_product, values in v.items()}
    return resh


resh = srzn(s)
for tek_product, h in resh.items():
    print(f"Среднее значение продаж для {tek_product}: {h:.2f} кг")
