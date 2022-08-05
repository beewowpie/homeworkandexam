# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.

a = ['abc', 'helloworld', 'python', 1, 2, 5, 3]
print(a)
b = []
n = []
f = open('my_file.txt', 'a')
for i in a:
    if type(i) is str:
        b.append(i)
    elif type (i) is int:
        i = int(i)
        n.append(i)
n.sort()
b.sort()
print(n)
print(b)

for i in b:
    f.write(i+ '\n')
for i in n:
    i = str(i)
    f.write(i+ '\n')
f.close()
r = open('my_file.txt')
s = r.readlines()
print(s)
r.close()