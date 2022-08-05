# 4. Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.



a = [1,2,5,8,2,3,7,2,9]
b = []
if a.count(2)>2 in a:
    b.append(2)
    print(b)


list_1 = [1, 55, 2, 3, 55, 55 , 55]
list_2 = []
for numbers in list_1:
    if list_1.count(numbers) >= 2:
        list_2.append(numbers)
print(list_2)