# 6 В строке “Иван Иванов” поменяйте местами слова.
# Может быть предоставлена любая строка с именем и фамилией.

a = "Шидловский Сергей"
b = a.split()
b.reverse()
result = " ".join(b)
print(result)