from math import floor
tournaments = int(input())
starting_points = int(input())

total_points = 0
won_counter = 0

for number in range(0, tournaments):
    stage = input()

    if stage == "W":
        total_points += 2000
        won_counter += 1
    elif stage == "F":
        total_points += 1200
    else:
        total_points += 720

average_points = floor(total_points / tournaments)
won_tournaments = won_counter / tournaments * 100

print(f"Final points: {total_points + starting_points}")
print(f"Average points: {average_points:.0f}")
print(f"{won_tournaments:.2f}%")

