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
