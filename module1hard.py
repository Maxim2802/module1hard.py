# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# вариант поиска в интернете( цикл)
def get_aver_grade(students: set, grades: list) -> dict:
    grades_of_students = {}
    students = sorted(students)
    for int in range(len(students)):
        grades_of_students[students[int]] = sum(grades[int]) / len(grades[int])
    return grades_of_students

res = get_aver_grade(students, grades)
print(res)

# вариант по изученому материалу

student_list = sorted(students)
the_average_value = [(sum(grades[0]) / len(grades[0])),
                     (sum(grades[1]) / len(grades[1])),
                     (sum(grades[2]) / len(grades[2])),
                     (sum(grades[3]) / len(grades[3])),
                     (sum(grades[4]) / len(grades[4]))]
the_average_value_student = dict(zip(student_list, the_average_value))
print(the_average_value_student)