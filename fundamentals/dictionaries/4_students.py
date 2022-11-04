courses_info = {}

command = input()

while ':' in command:
    student_information = command.split(':')
    name, id, course = student_information[0], student_information[1], student_information[2]
    if course not in courses_info.keys():
        courses_info[course] = {}

    courses_info[course][id] = name
    command = input()
name_of_course = ' '.join(command.split('_'))
if name_of_course in courses_info.keys():
    for (id, name) in courses_info[name_of_course].items():
        print(f'{name} - {id}')
