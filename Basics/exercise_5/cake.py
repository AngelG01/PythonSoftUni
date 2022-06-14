side_a = int(input())
side_b = int(input())

total = side_a * side_b

while total > 0:
    command = input()

    if command != "STOP":
        pieces = int(command)
        total -= pieces
        continue
    break
if total < 0:
    print(f"No more cake left! You need {abs(total)} pieces more.")
else:
    print(f"{total} pieces are left.")