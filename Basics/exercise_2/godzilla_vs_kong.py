budget = float(input())
people = int(input())
price_of_clothes_per_person = float(input())

decor_price = budget * 0.1
clothes_price = people * price_of_clothes_per_person

if people >= 150:
    clothes_price = clothes_price - clothes_price * 0.1

total_price = decor_price + clothes_price

if total_price <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - total_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {total_price - budget:.2f} leva more.")

