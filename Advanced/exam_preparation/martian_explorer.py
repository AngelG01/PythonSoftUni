def map_navigation(direction):
    new_row, new_col = [
        rover_position[0] + directions[direction][0] * -5,
        rover_position[1] + directions[direction][1] * -5,

    ]
    return [new_row, new_col]


matrix = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}
rover_position = []

water_deposit = False
metal_deposit = False
concrete_deposit = False

for r in range(6):
    c = input().split()
    matrix.append(c)
    if 'E' in c:
        rover_position.append(r)
        rover_position.append(c.index('E'))

commands = input().split(', ')

for curr_command in commands:
    row, col = [
        rover_position[0] + directions[curr_command][0],
        rover_position[1] + directions[curr_command][1],
    ]
    if 0 <= row < 6 and 0 <= col < 6:
        position = matrix[row][col]
        rover_position = [row, col]
    else:
        new_row, new_col = map_navigation(curr_command)
        position = matrix[new_row][new_col]
        rover_position = [new_row, new_col]

    if position == 'W':
        water_deposit = True
        print(f'Water deposit found at ({rover_position[0]}, {rover_position[1]})')
    elif position == 'M':
        metal_deposit = True
        print(f'Metal deposit found at ({rover_position[0]}, {rover_position[1]})')
    elif position == 'C':
        concrete_deposit = True
        print(f'Concrete deposit found at ({rover_position[0]}, {rover_position[1]})')
    elif position == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        break

if water_deposit and metal_deposit and concrete_deposit:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
