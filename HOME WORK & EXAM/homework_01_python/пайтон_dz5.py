# 5.* Вычислить сумму цифр случайного трёхзначного числа.
# (прочитать про модуль math и random)

from random import randint

summa=randint(100,999)
print(summa)
xxx=summa//100
xx=(summa//10)%10
x=summa%10

print(xxx+xx+x)