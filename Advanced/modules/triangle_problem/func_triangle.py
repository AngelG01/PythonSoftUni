def print_triangle(size):
    for i in range(2, size + 1):
        for n in range(1, i, 1):
            print(n, end='')
        print()

    for j in range(size - 1, 1, -1):
        for k in range(1, j, 1):
            print(k, end='')
        print()
