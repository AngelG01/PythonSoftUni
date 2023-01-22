rows, columns = [int(x) for x in input().split()]

start = 97

for row in range(rows):
    for column in range(columns):
        print(chr(start + row) + chr(start + row + column) + chr(start + row), end=' ')
    print()


# INPUT:
# 4 6
#
# -----
# 3 2