# 2. Разделить строку “Apples, Oranges, Pears, Bananas, Berries”
# по запятым и вывести на экран.
# Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.



art = "Apples, Oranges, Pears, Bananas, Berries"

art1 = ",".join(art)

art2 = art.replace(","," ")

print(art1)

print(art2)