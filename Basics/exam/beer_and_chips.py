from math import ceil

name = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())

price_of_beers = beers_count * 1.2
chips_price = price_of_beers * 0.45
price_of_chips = ceil(chips_price * chips_count)
total = price_of_chips + price_of_beers

left_money = budget - total
needed = total - budget
if total <= budget:
    print(f"{name} bought a snack and has {left_money:.2f} leva left.")
else:
    print(f"{name} needs {needed:.2f} more leva!")
