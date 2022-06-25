command = input()
kid_counter = 0
adult_counter = 0

while command != "Christmas":
    age = int(command)

    if age <= 16:
        kid_counter += 1
    else:
        adult_counter += 1

    command = input()

money_for_toys = kid_counter * 5
money_for_sweaters = adult_counter * 15

print(f"Number of adults: {adult_counter}")
print(f"Number of kids: {kid_counter}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")