# Задача №1
# Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.

import random

# n = int(input('Введите значение n: '))
# m = int(input('Введите значение m: '))
n,m = 5,5

a = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(10,99)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

N_1 = sum(a[0])
N_2 = sum(a[1])
N_3 = sum(a[2])
N_4 = sum(a[3])
N_5 = sum(a[4])

x = max(N_1,N_2, N_3, N_4, N_5)

if x == N_1:
    print('Максимальная сумма элементов находится в строке № 1!')
if x == N_2:
    print('Максимальная сумма элементов находится в строке № 2!')
if x == N_3:
    print('Максимальная сумма элементов находится в строке № 3!')
if x == N_4:
    print('Максимальная сумма элементов находится в строке № 4!')
if x == N_5:
    print('Максимальная сумма элементов находится в строке № 5!')

print('Сумма всех элементов этой строки: ',x)