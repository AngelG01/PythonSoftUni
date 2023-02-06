number_of_presents = int(input())
size = int(input())
santa_position = []
matrix = []
number_of_nice_kids = 0
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    colum = input().split()
    matrix.append(colum)

    if 'S' in colum:
        santa_position.append(r)
        santa_position.append(colum.index('S'))

        matrix[r][santa_position[1]] = '-'

command = input()

while command != 'Christmas morning':
    row = santa_position[0] + moves[command][0]
    col = santa_position[1] + moves[command][1]

    if 0 <= row < size and 0 <= col < size:
        santa_position = [row, col]

    if matrix[row][col] == 'V':
        number_of_presents -= 1
        number_of_nice_kids += 1
    elif matrix[row][col] == 'C':
        for check_direction in moves.keys():
            check_row, check_col = [
                row + moves[check_direction][0],
                col + moves[check_direction][1]
            ]

            check_position = matrix[check_row][check_col]

            if check_position == 'V' or check_position == 'X':
                if number_of_presents > 0:
                    number_of_presents -= 1
                    if check_position == 'V':
                        number_of_nice_kids += 1

            matrix[check_row][check_col] = '-'

    if number_of_presents == 0:
        break

    matrix[row][col] = '-'
    command = input()
matrix[santa_position[0]][santa_position[1]] = 'S'

non_happy_kids = 0
for colum in matrix:
    if 'V' in colum:
        non_happy_kids += colum.count('V')

if non_happy_kids > 0:
    print('Santa ran out of presents!')

for r in matrix:
    print(*r)

if non_happy_kids > 0:
    print(f'No presents for {non_happy_kids} nice kid/s.')
else:
    print(f'Good job, Santa! {number_of_nice_kids} happy nice kid/s.')
