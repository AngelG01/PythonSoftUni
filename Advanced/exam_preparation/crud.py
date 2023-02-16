matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(6):
    c = input().split()
    matrix.append(c)

staring_position = list(map(int, input().strip('(').strip(')').split(', ')))

commands = input().split(', ')

while commands[0] != 'Stop':
    command, direction = commands[0], commands[1]

    row, col = [
        staring_position[0] + directions[direction][0],
        staring_position[1] + directions[direction][1],
    ]

    if 0 <= row < 6 and 0 <= col < 6:
        position = matrix[row][col]
        staring_position = [row, col]
        if command == 'Create':
            if position == '.':
                value = commands[2]
                matrix[row][col] = value

        elif command == 'Update':
            if position != '.':
                value = commands[2]
                matrix[row][col] = value

        elif command == 'Delete':
            if position != '.':
                matrix[row][col] = '.'

        elif command == 'Read':
            if position != '.':
                print(position)

    commands = input().split(', ')

for ro in matrix:
    print(*ro)
