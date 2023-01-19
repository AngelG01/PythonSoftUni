number_of_rows = int(input())

all_numbers = []
for row in range(number_of_rows):
    row_data = list(map(int, input().split(', ')))

    for element in range(len(row_data)):
        all_numbers.append(row_data[element])

print(all_numbers)


# INPUT:
# 3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99