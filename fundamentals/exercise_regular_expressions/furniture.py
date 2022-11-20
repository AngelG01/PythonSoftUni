import re

command = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
furniture = []
total_money = 0

while command != 'Purchase':
    match = re.search(pattern, command)

    if match:
        product, price, count = match.groups()

        furniture.append(product)
        total_money += float(price) * int(count)

    command = input()

print('Bought furniture:')
if furniture:
    print('\n'.join(furniture))
print(f'Total money spend: {total_money:.2f}')
