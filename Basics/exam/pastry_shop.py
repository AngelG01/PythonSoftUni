type = input()
count = int(input())
day_of_the_month = int(input())
price = 0

if day_of_the_month <= 15:
    if type == "Cake":
        price = 24
    elif type == "Souffle":
        price = 6.66
    else:
        price = 12.6
else:
    if type == "Cake":
        price = 28.7
    elif type == "Souffle":
        price = 9.8
    else:
        price = 16.98

total = price * count

if day_of_the_month <= 22:
    if 100 <= total <= 200:
        total -= (total * 0.15)
    elif total > 200:
        total -= (total * 0.25)

    if day_of_the_month <= 15:
        total -= (total * 0.1)

print(f"{total:.2f}")

