r, c = list(map(int, input().split()))

matrix = []
my_position = []
touched_people = 0
moves_counter = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for ro in range(r):
    co = input().split()
    matrix.append(co)
    if 'B' in co:
        my_position.append(ro)
        my_position.append(co.index('B'))

matrix[my_position[0]][my_position[1]] = '-'

command = input()

while command != 'Finish':
    row, col = [
        my_position[0] + directions[command][0],
        my_position[1] + directions[command][1],
    ]

    if 0 <= row < r and 0 <= col < c:

        position = matrix[row][col]

        if position == '-':
            my_position = [row, col]
            moves_counter += 1
        elif position == 'P':
            touched_people += 1
            moves_counter += 1
            my_position = [row, col]
            matrix[row][col] = '-'
    if touched_people == 3:
        break

    command = input()

print('Game over!')
print(f'Touched opponents: {touched_people} Moves made: {moves_counter}')
