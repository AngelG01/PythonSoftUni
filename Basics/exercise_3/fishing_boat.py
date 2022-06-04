budget = int(input())
season = input()
fisherman = int(input())

price = 0
discount = 0

if season == "Spring":
    price = 3000
elif season == "Autumn" or season == "Summer":
    price = 4200
elif season == "Winter":
    price = 2600

if fisherman <= 6:
    discount = 0.1
elif 7 < fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

total_price = price - (discount * price)

if season != "Autumn" and fisherman % 2 == 0:
    total_price -= total_price * 0.05

if budget >= total_price:
    print(f"Yes! You have {budget - total_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_price-budget:.2f} leva.")

