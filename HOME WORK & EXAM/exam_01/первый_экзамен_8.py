
# 8.Вам передан массив чисел.
# Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5

b = int(input("Введите число: "))

a = [1, 5, 2, 9, 2, 9, 1]

if b not in a:
    print("Такого числа нет в списке: ", b)


if a.count(b) < 2:
    print("У этого числа нет пары: ", b)


elif a.count(b) == 2:
    print("У этого числа есть пара: ", b)