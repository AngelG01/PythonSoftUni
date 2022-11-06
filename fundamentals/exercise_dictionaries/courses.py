data_base = {}
command = input().split(' : ')

while command[0] != 'end':
    course = command[0]
    name = command[1]

    if course not in data_base:
        data_base[course] = []
    data_base[course].append(name)
    command = input().split(' : ')
for key, people in data_base.items():
    print(f'{key}: {len(people)}')
    for person in people:
        print(f'-- {person}')

