stocks = {}
command = input().split()
while True:

    if command[0] == 'buy':
        break

    product, price, quantity = command[0], float(command[1]), int(command[2])

    if product not in stocks.keys():
        stocks[product] = []
        stocks[product].append(price)
        stocks[product].append(quantity)
    else:
        stocks[product][0] = price
        stocks[product][1] += quantity
    command = input().split()

for elements in stocks:
    total_price = stocks[elements][0] * stocks[elements][1]
    print(f'{elements} -> {total_price:.2f}')

