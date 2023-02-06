size = int(input())

matrix = []
submarine_position = []
mines_hit = 0
cruisers_count = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    column = input()
    matrix.append(column)

    if 'S' in column:
        submarine_position.append(r)
        submarine_position.append(matrix[r].index('S'))
    cruisers_count += matrix[r].count('C')
matrix[submarine_position[0]] = matrix[submarine_position[0]][:submarine_position[1]] + '-' + matrix[submarine_position[
    0]][submarine_position[1] + 1:]

while mines_hit != 3:
    command = input()

    row, col = [
        submarine_position[0] + moves[command][0],
        submarine_position[1] + moves[command][1],
    ]

    if 0 <= row < size and 0 <= col < size:
        submarine_position = [row, col]
        position = matrix[row][col]

        if position == '*':
            mines_hit += 1

        elif position == 'C':
            cruisers_count -= 1

        matrix[row] = matrix[row][:col] + '-' + matrix[row][col + 1:]
        if cruisers_count == 0:
            break

matrix[submarine_position[0]] = matrix[submarine_position[0]][:submarine_position[1]] + 'S' + matrix[submarine_position[
    0]][submarine_position[1] + 1:]

if cruisers_count == 0:
    print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
else:
    print(f'Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!')

for curr_row in matrix:
    print(curr_row)