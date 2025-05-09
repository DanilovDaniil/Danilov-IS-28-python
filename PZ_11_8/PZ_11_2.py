# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.


f1 = open('text18-8 (2).txt', 'r', encoding='UTF-8')
c = f1.read()
print("Содержимое файла:")
print(c)
f1.close()

f1 = open('text18-8 (2).txt', 'r', encoding='UTF-8')
p = 0
for i in f1:
    for j in i:
        if j.isalpha():
            p += 1
f1.close()

print("Количество букв: ", p)

f1 = open('text18-8 (2).txt', 'r', encoding='UTF-8')
f2 = open('text_new.txt', 'w', encoding='UTF-8')
for i in f1:
    m = i.replace('с', '').replace('С', '')
    f2.write(m)
f1.close()
f2.close()