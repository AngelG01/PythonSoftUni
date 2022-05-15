chicken_count = int(input())
fish_count = int(input())
vegan_count = int(input())

total_price = chicken_count * 10.35 + fish_count * 12.4 + vegan_count * 8.15
dessert_price = total_price * 0.2
final_price = total_price + dessert_price + 2.5

print(f"{final_price:.2f}")
