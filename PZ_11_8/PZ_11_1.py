# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине:


p = ['-99 6 12 -36 20 45 100 -15 8 17 -5 23']
f3 = open('data_3.txt', 'w', encoding='UTF-8')
f3.writelines(p)
f3.close()

f4 = open('data_4.txt', 'w', encoding='UTF-8')
f4.write('Исходные данные: ')
f4.writelines(p)
f4.close()

f3 = open('data_3.txt', encoding='UTF-8')
k = f3.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

count = len(p)
min_value = min(k)
last_min = len(k) - 1 - k[::-1].index(min_value)

h = len(k) // 2
d10 = 0
for i in k[h:]:
    if i > 10:
        d10 += i

f4 = open('data_4.txt', 'a', encoding='UTF-8')
f4.write('\n')
print('Количество элементов:', count, file=f4)
print('Индекс последнего минимального элемента', last_min, file=f4)
print('Сумма элементов больших 10 во второй половине:', d10, file=f4)
f4.close()
