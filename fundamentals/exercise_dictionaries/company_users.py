command = input().split(' -> ')
data_base = {}
while command[0] != 'End':
    company, id = command[0], command[1]
    if company not in data_base.keys():
        data_base[company] = []
    if id not in data_base[company]:
        data_base[company].append(id)

    command = input().split(' -> ')

for name_of_company, people in data_base.items():
    print(name_of_company)
    for person in people:
        print(f'-- {person}')

