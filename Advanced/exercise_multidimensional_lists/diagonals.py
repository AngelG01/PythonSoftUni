rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

primary_d = []
secondary_d = []

# main diagonal:
step = len(matrix) - 1
for curr in range(len(matrix)):
    for col in range(len(matrix)):
        primary_d.append(matrix[curr][curr])
        break

# secondary diagonal:
for sec_curr in range(len(matrix)):
    for sec_col in range(step, -1, -1):
        secondary_d.append(matrix[sec_curr][step])
        step -= 1
        break

print(f'Primary diagonal: {", ".join([str(x) for x in primary_d])}. Sum: {sum(primary_d)}')
print(f'Secondary diagonal: {", ".join([str(x) for x in secondary_d])}. Sum: {sum(secondary_d)}')
