cats_count = int(input())
gram = 0
group1 = 0
group2 = 0
group3 = 0

total_gram = 0

for current_cat in range(0, cats_count):
    gram = float(input())

    if 100 <= gram < 200:
        group1 += 1
    elif 200 <= gram < 300:
        group2 += 1
    elif 300 <= gram < 400:
        group3 += 1

    total_gram += gram

total_price = total_gram / 1000 * 12.45

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_price:.2f} lv.")

