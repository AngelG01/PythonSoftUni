change = float(input())
coins_change = round(change * 100)
coins = 0
while coins_change > 0:

    if coins_change - 200 >= 0:
        coins_change -= 200
        coins += 1
    elif coins_change - 100 >= 0:
        coins_change -= 100
        coins += 1
    elif coins_change - 50 >= 0:
        coins_change -= 50
        coins += 1
    elif coins_change - 20 >= 0:
        coins_change -= 20
        coins += 1
    elif coins_change - 10 >= 0:
        coins_change -= 10
        coins += 1
    elif coins_change - 5 >= 0:
        coins_change -= 5
        coins += 1
    elif coins_change - 2 >= 0:
        coins_change -= 2
        coins += 1
    else:
        coins_change -= 1
        coins += 1

print(coins)
