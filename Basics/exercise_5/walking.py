walking = input()
goal = 10000
total = 0

while total < goal:
    if walking != "Going home":
        steps = int(walking)
    else:
        to_home_steps = int(input())
        total += to_home_steps
        break

    total += steps
    if total <= goal:
        walking = input()

diff = goal - total
if total >= goal:
    print("Goal reached! Good job!")
    print(f"{total - goal} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
