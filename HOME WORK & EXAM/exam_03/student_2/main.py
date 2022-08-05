from school import School
from student import Student


student_1 = Student("Denis", "1A", [7, 7, 8, 7, 8])
student_2 = Student("Artem", "1B", [8, 10, 5, 9, 9])

school_1 = School([])

school_1.admission(student_1)  # добавляем студента
school_1.admission(student_2)

print(school_1.get_list_of_students())  # получаем список студентов
print(school_1.get_list_automate_students())  # получаем список автоматов

print(school_1.get_list_of_student_with_needed_mark([7, 8]))  # выводит студента с нужно оценкой
print(school_1.print_group("1A"))  # вывод учеников одной группы