numbers = map(int, input().split())


def check_even(element):
    if element % 2 == 0:
        return True
    return False


even_numbers = filter(check_even, numbers)

final = list(even_numbers)

print(final)

