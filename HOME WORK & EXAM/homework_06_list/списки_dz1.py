# 1 Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность.
# Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.


l = [15, 48, "hello", 6, 19, "world"]



l[0] = 1
print("нечётное 15 заменили на 1: " + str(l))

n1 = l[1]
s1 = 0

while n1 > 0:

    s1 += n1 % 10
    n1 = n1 // 10

print("чётное 48 подсчитали сумму его цифр: " +str(s1))


n4 = l[4]
s4 = 0

while n4 > 0:

    s4 += n4 % 10
    n4 = n4 // 10

print("чётное 19 подсчитали сумму его цифр: " +str(s4))


list=[15,48,'hello',6,19,'world']
f = 0
w = 0
v = 0
for i in list:
    if type(i) is int:
        if i % 2 == 0:
            i = str(i)
            for k in i:
                k = int(k)
                f+=k
            print(i,"Сумма цифр: ", f, "\n")
        else:
            index = list.index(i)
            list[index] = 1
    elif type (i) is str:
        for r in i:
            if r in "aeoiu":
                w += 1
            else:
                v += 1
        print(i, "\nКоличество гласных букв: ", w)
        print("Количество согласных: ", v, "\n")
        w = 0
        v = 0
print(list)

