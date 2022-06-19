command = input()
days = 1
reached = 5364
not_reached = True
while command != "END" and days != 5:
    days += 1
    distance = int(input())
    reached += distance
    if command == "No":
        days -= 1

    if reached >= 8848:
        not_reached = False
        break

    command = input()

if not_reached:
    print("Failed!")
    print(reached)
else:
    print(f"Goal reached for {days} days!")

