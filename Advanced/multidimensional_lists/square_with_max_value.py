number_of_rows = [int(x) for x in input().split(', ')]

matrix = []
for row in range(number_of_rows[0]):
    row_data = [int(x) for x in input().split(', ')]
    matrix.append(row_data)

max_values = []
square_value = []
for curr_data in matrix:
    index = 0
    for curr in curr_data:

        highest = max(curr_data)
        max_values.append(highest)
        curr_data.remove(highest)
        index += 1
        if index == 2:
            break

for _ in range(4):
    top = max(max_values)
    square_value.append(top)
    max_values.remove(top)

print(square_value)
print(sum(square_value))