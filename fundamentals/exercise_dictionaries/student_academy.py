count_of_students = int(input())
student_info = {}

for i in range(count_of_students):
    name = input()
    grade = float(input())

    if name not in student_info:
        student_info[name] = []
    student_info[name].append(grade)

for student in student_info:
    average_grade = sum(student_info[student]) / len(student_info[student])
    if average_grade >= 4.5:
        print(f'{student} -> {average_grade:.2f}')
