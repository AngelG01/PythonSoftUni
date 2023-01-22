rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

command = input().split()

while command[0] != 'END':

    current = command[0]

    if current == 'swap' and len(command) == 5:
        row1 = int(command[1])
        col1 = int(command[2])
        row2 = int(command[3])
        col2 = int(command[4])

        if 0 <= row1 < rows and 0 <= col1 < columns and 0 <= row2 < rows and 0 <= col2 < columns:
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            print(*[' '. join(str(matrix[r][c]) for c in range(columns)) for r in range(rows)], sep='\n')
        else:
            print(f'Invalid input!')
    else:
        print('Invalid input!')

    command = input().split()


# INPUT:
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
#
# --------------
#
# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END