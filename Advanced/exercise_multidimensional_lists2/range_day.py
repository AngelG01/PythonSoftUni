my_position = []
matrix = []
hitted_targets = []
for r in range(5):
    matrix.append(input().split())

    if 'A' in matrix[r]:
        my_position.append(r)
        my_position.append(matrix[r].index('A'))
        matrix[r][my_position[1]] = '.'

number_of_commands = int(input())

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
check_if_training_didnt_end = True
left_targets = 0
for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'move':
        direction = command[1]
        steps = int(command[2])

        row = my_position[0] + (moves[direction][0] * steps)
        col = my_position[1] + (moves[direction][1] * steps)

        if not (0 <= row < 5 and 0 <= col < 5):
            continue

        position = matrix[row][col]

        if position == '.':
            my_position = [row, col]

    elif command[0] == 'shoot':
        direction_to_shoot = command[1]

        row_to_shoot = my_position[0]
        col_to_shoot = my_position[1]

        while 0 <= row_to_shoot < 5 and 0 <= col_to_shoot < 5:

            row_to_shoot += moves[direction_to_shoot][0]
            col_to_shoot += moves[direction_to_shoot][1]

            if 0 <= row_to_shoot < 5 and 0 <= col_to_shoot < 5:
                position_to_shoot = matrix[row_to_shoot][col_to_shoot]
                if position_to_shoot == 'x':
                    hitted_targets.append([row_to_shoot, col_to_shoot])
                    matrix[row_to_shoot][col_to_shoot] = '.'
                    break
        for row in range(5):
            if 'x' in matrix[row]:
                check_if_training_didnt_end = False
        if check_if_training_didnt_end:
            break

training_done = True

for x in range(5):
    if 'x' in matrix[x]:
        training_done = False
        left_targets += matrix[x].count('x')

if training_done:
    print(f'Training completed! All {len(hitted_targets)} targets hit.')
else:
    print(f'Training not completed! {left_targets} targets left.')
if hitted_targets:
    print(*hitted_targets, sep='\n')
