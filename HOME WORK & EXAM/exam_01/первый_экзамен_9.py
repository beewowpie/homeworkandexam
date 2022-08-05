# 9.	Дан список [student1, student2, student3]
# с помощью цикла for добавить к каждому элементу списка слово “_good”. Вывести на экран.

s = ["student1", "student2", "student3"]

s1 = []

for i in s:
    s1.append( i + "_good")

print(s1)