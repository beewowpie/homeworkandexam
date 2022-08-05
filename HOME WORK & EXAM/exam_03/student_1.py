# 2.Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Необходимо понять у кого больше всего денег и вернуть его имя.
# Если у студентов денег поровну вернуть: “all”.

class Student:
    # Класс студен описан следующим образом:
    def __init__(self, name, money):
        self.name = name
        self.money = money

student1 = Student("Artem", 100)
student2 = Student("Dzenis", 80)
student3 = Student("Nikita", 90)
students = [student1, student2, student3]
moneys = []
for student in students:
    moneys.append((student.money))

count = moneys.count(moneys[0])
if count == len(students):
    print("all")
else:
    max_money = 0
    student_name = ""
    for student in students:
        if student.money > max_money:
            max_money = student.money
            student_name = student.name
    print(max_money, student_name)
print(moneys)