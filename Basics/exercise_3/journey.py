budget = float(input())
season = input()

vacation_price = 0
location = ""

place = ""

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        vacation_price = budget * 0.3
    elif season == "winter":
        vacation_price = budget * 0.7
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        vacation_price = budget * 0.4
    elif season == "winter":
        vacation_price = budget * 0.8
else:
    location = "Europe"
    vacation_price = budget * 0.9

if season == "summer":
    place = "Camp"
else:
    place = "Hotel"

if budget > 1000:
    place = "Hotel"

print(f"Somewhere in {location}")
print(f"{place} - {vacation_price:.2f}")
