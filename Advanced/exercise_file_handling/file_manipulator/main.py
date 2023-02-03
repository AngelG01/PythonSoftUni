import os

command = input().split('-')

while command[0] != 'End':

    if command[0] == 'Create':
        file_name = command[1]
        with open(f'{file_name}', 'w') as new_file:
            new_file.write('')

    elif command[0] == 'Add':
        file_name = command[1]
        content = command[2]
        with open(f'{file_name}', 'a') as add_to_file:
            add_to_file.write(content + '\n')

    elif command[0] == 'Replace':

        file_name = command[1]
        old_string = command[2]
        new_string = command[3]
        try:
            with open(f'{file_name}', 'r') as file:
                file = file.readlines()
            for line in range(len(file)):
                file[line] = file[line].replace(old_string, new_string)

            with open(f'{file_name}', 'w') as edited_file:
                edited_file.write(''.join(file))
        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':
        file_name = command[1]

        try:
            os.remove(f'{file_name}')
        except FileNotFoundError:
            print('An error occurred')
    command = input().split('-')

