size = int(input())

field = []
bunny_position = []
best_path = []

best_direction = None
max_collected_eggs = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    field.append(input().split())

    if 'B' in field[row]:
        bunny_position = [row, field[row].index('B')]

for direction, positions in moves.items():
    row, col = [
        bunny_position[0] + positions[0],
        bunny_position[1] + positions[1],
    ]
    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == 'X':
            break
        collected_eggs += int(field[row][col])
        path.append([row,col])

        row += positions[0]
        col += positions[1]

        if collected_eggs >= max_collected_eggs:
            max_collected_eggs = collected_eggs
            best_direction = direction
            best_path = path


print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)