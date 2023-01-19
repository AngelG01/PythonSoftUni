matrix_rows = int(input())
matrix = []
for row in range(matrix_rows):
    row_data = list(map(int, input().split(', ')))
    matrix.append(row_data)

even_numbers = []

for current_row in range(len(matrix)):
    new_matrix = []
    for current_number in matrix[current_row]:
        if current_number %2 == 0:
            new_matrix.append(current_number)

    even_numbers.append(new_matrix)



print(even_numbers)

# INPUT:
# 4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67