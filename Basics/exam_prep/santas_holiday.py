count = int(input()) - 1
type_of_room = input()
pos_or_neg = input()

discount = 0
price = 0

if type_of_room == "apartment":
    price = 25
    if count < 10:
        discount = 0.3
    elif 10 <= count <= 15:
        discount = 0.35
    else:
        discount = 0.5
elif type_of_room == "president apartment":
    price = 35
    if count < 10:
        discount = 0.1
    elif 10 <= count <= 15:
        discount = 0.15
    else:
        discount = 0.2
else:
    price = 18

total_price = (price * count)
final_price = total_price - (total_price * discount)

if pos_or_neg == "positive":
    final_price += final_price * 0.25
else:
    final_price -= final_price * 0.1

print(f"{final_price:.2f}")

