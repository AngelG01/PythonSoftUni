locations_count = int(input())

for current_location in range(0, locations_count):
    expected_gold = float(input())
    days = int(input())
    mined_gold = 0

    for current_day in range(0, days):
        today_gold = float(input())
        mined_gold += today_gold

    average_gold = mined_gold / days
    needed = expected_gold - mined_gold / days

    if average_gold >= expected_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        print(f"You need {needed:.2f} gold.")

