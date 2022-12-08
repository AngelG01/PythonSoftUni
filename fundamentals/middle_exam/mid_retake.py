money_per_view = float(input())
number_of_users = int(input())
total_money = 0
for person in range(1, number_of_users + 1):
    views = int(input())
    if views == 1:
        continue

    if person % 3 == 0:
        if views > 5:
            total_money += views * ((2 * money_per_view) * 3)
        else:
            total_money += views * (money_per_view * 3)
    else:
        if views > 5:
            total_money += views * (money_per_view * 2)
        else:
            total_money += views * money_per_view


print(f'Total money earned: {total_money:.2f}')
