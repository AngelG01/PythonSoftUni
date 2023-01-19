square_matrix = int(input())
matrix = []

for row in range(square_matrix):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)
total = 0
for row in range(square_matrix):
    for column in range(row, square_matrix):
        total += matrix[row][column]
        break


print(total)

# INPUT:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12