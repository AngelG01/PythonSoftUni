cells_information = input().split("#")
water_amount = int(input())
effort = 0
fire_putted_out = 0

numbers = []
fire_level = []
cells_extinguished = []

for current_cell in cells_information:

    for word in current_cell.split():
        if word.isdigit():
            numbers.append(int(word))
    for level in current_cell.split():
        fire_level.append(level)
        break

for current in range(len(cells_information)):
    isValid = False

    if 81 <= numbers[current] <= 125 and fire_level[current] == "High":
        isValid = True
    elif 51 <= numbers[current] <= 80 and fire_level[current] == "Medium":
        isValid = True
    elif 1 <= numbers[current] <= 50 and fire_level[current] == "Low":
        isValid = True

    if isValid:
        water_amount -= numbers[current]
        if water_amount >= 0:
            effort += numbers[current] * 0.25
            fire_putted_out += numbers[current]
            cells_extinguished.append(cells_information[current])
        else:
            water_amount += numbers[current]

print("Cells:")
for number in cells_extinguished:
    for word in number.split():
        if word.isdigit():
            print(f" - {word}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_putted_out}")
