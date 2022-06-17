destination = input()

while destination != "End":
    money_needed = float(input())
    saved = 0
    while saved < money_needed:
        current_money = float(input())
        saved += current_money
    print(f"Going to {destination}!")
    destination = input()

