number_of_rows, number_of_columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(number_of_rows):
    row_data = list(map(int, input().split(' ')))
    matrix.append(row_data)

column_sums = []

for column_index in range(number_of_columns):
    column_sum = 0
    for row_index in range(number_of_rows):
        column_sum += matrix[row_index][column_index]
    column_sums.append(column_sum)
print(*column_sums, sep='\n')

# INPUT:
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0