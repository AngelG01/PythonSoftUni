number_of_presents = int(input())
size = int(input())
santa_position = []
matrix = []
gifts_given = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    matrix.append(input().split())

    if 'S' in matrix[r]:
        santa_position.append(r)
        santa_position.append(matrix[r].index('S'))
        matrix[r][santa_position[1]] = '-'

while number_of_presents > 0:
    direction = input()

    if direction == 'Christmas morning':
        break

    row, col = [
        santa_position[0] + moves[direction][0],
        santa_position[1] + moves[direction][1],
    ]

    if not (0 <= row < size and 0 <= col < size):
        continue
    position = matrix[row][col]

    if position == 'V':
        number_of_presents -= 1
        gifts_given += 1

    elif position == 'C':
        for check_direction in moves.keys():
            check_row, check_col = [
                row + moves[check_direction][0],
                col + moves[check_direction][1]
            ]
            check_position = matrix[check_row][check_col]

            if check_position == 'V' or check_position == 'X':
                if number_of_presents > 0:
                    gifts_given += 1
                    number_of_presents -= 1

            matrix[check_row][check_col] = '-'

    matrix[row][col] = '-'
    santa_position = [row, col]

matrix[santa_position[0]][santa_position[1]] = 'S'

if number_of_presents == 0:
    print('Santa ran out of presents!')
[print(*matrix[r]) for r in range(size)]
nice_kids_finish_first = True
no_present = 0
for row in range(size):
    if 'V' in matrix[row]:
        no_present += matrix[row].count('V')
        nice_kids_finish_first = False

if nice_kids_finish_first:
    print(f'Good job, Santa! {gifts_given} happy nice kid/s.')
else:
    print(f'No presents for {no_present} nice kid/s.')
