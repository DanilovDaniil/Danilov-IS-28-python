# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Сумма элементов больших 10 во второй половине:


f3 = open('data_3.txt', 'w', encoding='UTF-8')
print("-99, 6, 12, -36, 20, 45, 100, -15, 8, 17, -5, 23", file=f3)
f3.close()

f4 = open('data_4.txt', 'w', encoding='UTF-8')
f4.write('Исходные данные: ')
print("-99, 6, 12, -36, 20, 45, 100, -15, 8, 17, -5, 23", file=f4)
f4.close()

f3 = open('data_3.txt', 'r', encoding='UTF-8')
p = 0
for i in f3:
    n = i.split(',')
    p += len(n)
f3.close()

f3 = open('data_3.txt', 'r', encoding='UTF-8')
t = f3.read()

numbers = []
for i in t.split():
    numbers.append(i)

min_num = numbers[0]
last_index = 0

for i in range(len(numbers)):
    num = numbers[i]
    if num <= min_num:
        min_num = num
        last_index = i
f3.close()

f3 = open('data_3.txt', encoding='UTF-8')
k = f3.read()
k = k.split(', ') 
for i in range(len(k)):
    k[i] = int(k[i])
f3.close()

half = len(k) // 2
sum_gt10 = 0
for i in range(half, len(k)):
    if k[i] > 10:
        sum_gt10 += k[i]

f4 = open('data_4.txt', 'a', encoding='UTF-8')
print('Количество элементов:', p, file=f4)
print('Индекс последнего минимального элемента', last_index, file=f4)
print('Сумма элементов больших 10 во второй половине:', sum_gt10, file=f4)
f4.close()
