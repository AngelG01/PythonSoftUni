command = input()
phonebook = {}

while '-' in command:
    info = command.split('-')
    name, number = info[0], info[1]
    phonebook[name] = number
    command = input()

for i in range(int(command)):
    search_name = input()

    if search_name in phonebook.keys():
        print(f'{search_name} -> {phonebook[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')
