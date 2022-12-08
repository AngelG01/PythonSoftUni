text = input().split('|')

command = input().split()

while command[0] != 'Done':

    if command[0] == 'Add':
        particle = command[1]
        index = int(command[2])
        if index in range(0, len(text)):
            text.insert(index, particle)

    elif command[0] == 'Remove':
        index = int(command[1])
        if index in range(0, len(text)):
            text.remove(text[index])

    elif command[0] == 'Check':
        current = command[1]
        if current == 'Even':
            for element in range(len(text)):
                if element % 2 == 0:
                    print(f'{text[element]}', end=' ')
        elif current == 'Odd':
            for element in range(1, len(text)):
                if element % 2 != 0 or element == 1:
                    print(f'{text[element]}', end=' ')
        print()
    command = input().split()
print(f'You crafted {"".join(text)}!')
