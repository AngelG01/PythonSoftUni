def create_rhombus(size, star_count):
    for row in range(size - star_count):
        print(' ', end='')

    for row in range(1, star_count):
        print('*', end=' ')
    print('*')


size = int(input())

for star_count in range(1, size):
    create_rhombus(size, star_count)

for star_count in range(size, 0, -1):
    create_rhombus(size, star_count)
