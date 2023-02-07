def students_credits(*args):
    info = args
    total_credits = 0
    courses_credits = {}

    for curr_course in info:
        name, credit, max_points, student_points = curr_course.split('-')
        grade = int(student_points) / int(max_points)
        curr_credit = grade * int(credit)
        total_credits += curr_credit

        if name not in courses_credits.keys():
            courses_credits[name] = curr_credit

    sorted_grades = sorted(courses_credits.items(),
                           key=lambda x: -x[1])
    if total_credits >= 240:
        return f'Diyan gets a diploma with {total_credits:.1f} credits.' + '\n' + "\n".join(
            f"{k} - {v:.1f}" for k, v in sorted_grades)
    else:
        return f'Diyan needs {240 - total_credits:.1f} credits more for a diploma.' + '\n' + "\n".join(
            f"{k} - {v:.1f}" for k, v in sorted_grades)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
