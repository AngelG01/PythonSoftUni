size = int(input())
racing_number = input()
car_position = [0, 0]
matrix = []
total_distance = 0

for r in range(size):
    column = input().split(' ')
    matrix.append(column)

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

direction = input()


def search_for_tunnel(row, col):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'T':
                if r != row and c != col:
                    matrix[r][c] = '.'
                    return [r, c]


while True:

    if direction == 'End':
        print(f'Racing car {racing_number} DNF.')
        print(f'Distance covered {total_distance} km.')
        matrix[row][col] = 'C'
        [print(''.join(row)) for row in matrix]
        break

    row, col = [
        car_position[0] + moves[direction][0],
        car_position[1] + moves[direction][1],
    ]
    if 0 <= row < size and 0 <= col < size:

        curr_position = matrix[row][col]

        if curr_position == 'T':
            total_distance += 30
            matrix[row][col] = '.'
            car_position = search_for_tunnel(row, col)
        elif curr_position == 'F':
            total_distance += 10
            print(f'Racing car {racing_number} finished the stage!')
            print(f'Distance covered {total_distance} km.')
            matrix[row][col] = 'C'
            [print(''.join(row)) for row in matrix]
            break
        else:
            total_distance += 10
            car_position = [row, col]
    direction = input()
