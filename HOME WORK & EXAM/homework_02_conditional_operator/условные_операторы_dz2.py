# Задача №2: Определить существование треугольника и его тип

a=float(input("Сторона треугольника (a) = "))
b=float(input("Сторона треугольника (b) = "))
c=float(input("Сторона треугольника (с) = "))

if a+b<=c or a+c<=b or b+c<=a:
    print("Его не существует!!!")
elif a==b or b==c or a==c :
    print("Является равнобедренным!")
else:
    print("Является равносторонним!")