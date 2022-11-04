products = {}
count_of_elements = 0
quantity = 0

while True:
    command = input().split(': ')

    if command[0] == 'statistics':
        break

    key = command[0]
    value = int(command[1])

    quantity += value
    if key in products:
        products[key] += value
    else:
        products[key] = value
        count_of_elements += 1

print(f'Products in stock:')
for (product, storage) in products.items():
    print(f'- {product}: {storage}')
print(f'Total Products: {count_of_elements}')
print(f'Total Quantity: {quantity}')
