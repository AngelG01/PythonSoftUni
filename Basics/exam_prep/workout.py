from math import ceil

days = int(input())
kilometers = float(input())
bonus_distance = 0
total = 0
for number in range(1, days + 1):
    percentage = int(input())
    asd = kilometers + bonus_distance
    bonus_distance = bonus_distance + (asd * percentage / 100)
    total += kilometers + bonus_distance
final_total = total + kilometers
enough = final_total - 1000
not_enough = 1000 - final_total
if final_total >= 1000:
    print(f"You've done a great job running {ceil(enough):.0f} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(not_enough):.0f} more kilometers")
