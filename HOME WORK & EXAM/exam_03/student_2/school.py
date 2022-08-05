class School:

    def __init__(self, students):
        self.students = students

    def get_list_of_students(self):         # получить список студентов
        return self.students

    def admission(self, student):        # поступление в школу
        self.students.append(student)

    def remove(self, student, group):    # удаление из школы по группе
        if student.group == group:
            self.students.remove(student)

    def print_names(self):                  # написать имена студентов
        for student in self.students:
            print(student.name)

    def print_group(self, group):  # вывод учеников одной группы
        students = []
        for student in self.students:
            if student.group == group:
                students.append(student)
        return students

    def get_list_automate_students(self, auto_mark=7):  # студенты с нужным средним баллом
        list_automate = []
        for student in self.students:
            average_grade = sum(student.progress) / len(student.progress)
            if average_grade >= auto_mark:
                list_automate.append(student)
        return list_automate

    def get_list_of_student_with_needed_mark(self, grades):    # вывод учеников с определенными оценками
        list_std = self.students.copy()
        for student in self.students:
            for mark in student.progress:
                if mark not in grades:
                    list_std.remove(student)
                    break
        return list_std
