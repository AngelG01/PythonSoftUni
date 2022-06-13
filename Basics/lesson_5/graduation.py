name = input()

count = 1
total_grade = 0
excluded = 0
graduated = True
while count <= 12:
    grade = float(input())
    if grade < 4:
        excluded += 1
        if excluded > 1:
            graduated = False
            break
    else:
        count += 1
        total_grade += grade

if graduated:
    average_grade = total_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{name} has been excluded at {count} grade")
