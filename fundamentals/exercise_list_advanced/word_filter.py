words = input().split()

even_length = [x for x in words if len(x) % 2 == 0]

print('\n'.join(even_length))
