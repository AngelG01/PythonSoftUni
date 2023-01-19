def read_matrix():
    number_of_rows, number_of_columns = map(int, input().split(', '))
    current_matrix = []


    for row in range(number_of_rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix

matrix = read_matrix()
matrix_sum = 0

for row in range(len(matrix)):
    row_sum = sum(matrix[row])
    matrix_sum += row_sum

print(matrix_sum)
print(matrix)


# INPUT:
#
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0