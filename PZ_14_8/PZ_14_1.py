# В исходном текстовом файле(Dostoevsky.txt) найти все произведения писателя.
# Посчитать количество полученных элементов.

import re

f = open('Dostoevsky.txt', 'r', encoding='UTF-8')
text = f.read()
f.close()

works = re.findall(r'«([^»]+)»', text)

print(works, "\n")

print("Всего найдено произведений Достоевского:", len(works))
