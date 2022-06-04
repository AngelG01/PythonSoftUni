flower = input()
flowers_count = int(input())
budget = int(input())

price = 0
total_price = 0

if flower == "Roses":
    price = 5
    total_price = flowers_count * price

    if flowers_count > 80:
        total_price -= total_price * 0.1

elif flower == "Dahlias":
    price = 3.8
    total_price = flowers_count * price

    if flowers_count > 90:
        total_price -= total_price * 0.15

elif flower == "Tulips":
    price = 2.8
    total_price = flowers_count * price

    if flowers_count > 80:
        total_price -= total_price * 0.15

elif flower == "Narcissus":
    price = 3
    total_price = flowers_count * price

    if flowers_count < 120:
        total_price += total_price * 0.15

elif flower == "Gladiolus":
    price = 2.5
    total_price = flowers_count * price

    if flowers_count < 80:
        total_price += total_price * 0.2

enough = budget - total_price
not_enough = total_price - budget

if total_price <= budget:
    print(f"Hey, you have a great garden with {flowers_count} {flower} and {enough:.2f} leva left.")
else:
    print(f"Not enough money, you need {not_enough:.2f} leva more.")
