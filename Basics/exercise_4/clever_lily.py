ages = int(input())
washing_machine_price = float(input())
toy_price = int(input())

saved_money = 0
money_counter = 0
toys_counter = 0
taken = 0
for age in range(1, ages + 1):
    if age % 2 == 0:
        saved_money += 10
        money_counter += saved_money
        taken += 1
    else:
        toys_counter += 1

total = money_counter - taken + (toys_counter * toy_price)
enough = total - washing_machine_price
diff = washing_machine_price - total

if total >= washing_machine_price:
    print(f"Yes! {enough:.2f}")
else:
    print(f"No! {diff:.2f}")
