number_of_students = int(input())
students = {}
for _ in range(number_of_students):
    student_info = tuple(input().split())
    name, grade = student_info
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

[print(f'{name} -> {" ".join(f"{x:.2f}" for x in grades)} (avg: {sum(grades)/len(grades):.2f})') for name, grades in students.items()]

# INPUT:
# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00