number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
top_student = 0
for student in range(number_of_students):
    attendance_count = int(input())
    total_bonus = (attendance_count / number_of_lectures) * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus

    if attendance_count > top_student:
        top_student = attendance_count

print(f'Max Bonus: {round(max_bonus)}.')
print(f'The student has attended {top_student} lectures.')
