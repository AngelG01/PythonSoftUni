rows = int(input())
matrix = [[int(x) for x in input().split(' ')] for r in range(rows)]

command = input().split()

while command[0] != 'END':
    row = int(command[1])
    column = int(command[2])
    value = int(command[3])
    if 0 <= row < rows and 0 <= column < len(matrix[0]):
        if command[0] == 'Add':
            matrix[row][column] += value

        elif command[0] == 'Subtract':
            matrix[row][column] -= value
    else:
        print('Invalid coordinates')

    command = input().split()

for r in range(rows):
    for el in matrix[r]:
        print(el, end=' ')
    print()
