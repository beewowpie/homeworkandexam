# даны два целых числа m и n (m < n). напишите программу котороя выводит все числа от m до n включительно.

m = int(input("Введите число: "))
n = int(input("Введите число: "))

for i in range(m, n + 1, 1):
    print(i)