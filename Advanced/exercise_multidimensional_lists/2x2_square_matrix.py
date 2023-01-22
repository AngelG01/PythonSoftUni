rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]

twins = 0

for element in range(rows - 1):
    for column in range(columns - 1):
        twin_one = '1'
        twin_two = '2'

        if matrix[element][column] == matrix[element][column + 1]:
            twin_one = matrix[element][column], matrix[element][column + 1]
        if matrix[element + 1][column] == matrix[element + 1][column + 1]:
            twin_two = matrix[element + 1][column], matrix[element + 1][column + 1]

        if twin_one == twin_two:
            twins += 1
print(twins)
