number_of_orders = int(input())
total = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsul_per_day = int(input())

    order_price = (price_per_capsule * capsul_per_day) * days
    total += order_price

    if not 1 > days > 31 and 0.01 > price_per_capsule > 100 and 0 > capsul_per_day > 2000:
        print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")
