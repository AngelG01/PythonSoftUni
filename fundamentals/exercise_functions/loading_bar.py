percentage = int(input())


def counter(percentage: int):
    number_of_percents = percentage // 10
    number_of_dots = 10 - number_of_percents
    for i in range(number_of_percents):
        print("%", end="")
    for n in range(number_of_dots):
        print(".", end="")
    return ""


if percentage < 100:
    print(f'{percentage}% ', end='')
    print(f'[', end='')
    print(counter(percentage), end='')
    print(f']')
    print('Still loading...')
else:
    print(f'{percentage}% Complete!')
    print(f'[', end='')
    print(counter(percentage), end='')
    print(f']')
