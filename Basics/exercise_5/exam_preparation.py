count_of_bad_grades = int(input())
average_grade = 0
count = 0
failed = True
last_problem = ''
solved = 0

while count < count_of_bad_grades:
    task_name = input()

    if task_name == "Enough":
        failed = False
        break

    grade = int(input())
    if grade <= 4:
        count += 1

    average_grade += grade
    solved += 1
    last_problem = task_name

if failed:
    print(f"You need a break, {count} poor grades.")
else:
    print(f"Average score: {average_grade / solved:.2f}")
    print(f"Number of problems: {solved}")
    print(f"Last problem: {last_problem}")
