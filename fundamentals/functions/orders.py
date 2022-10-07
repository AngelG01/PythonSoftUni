order = input()
count = int(input())


def price_for_count(count: int, order: str):
    price = 0
    if order == 'water':
        price = 1
    elif order == 'coffee':
        price = 1.5
    elif order == 'coke':
        price = 1.4
    elif order == 'snacks':
        price = 2

    total = float(price * count)

    print(f'{total:.2f}')


price_for_count(count, order)
