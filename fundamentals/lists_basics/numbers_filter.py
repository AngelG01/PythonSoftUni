rotations = int(input())

numbers = []
filtered = []
for i in range(rotations):
    number = int(input())
    numbers.append(number)

command = input()

if command == "even":
    for current_number in numbers:
        if current_number % 2 == 0:
            filtered.append(current_number)
elif command == "odd":
    for current_number in numbers:
        if current_number % 2 != 0:
            filtered.append(current_number)
elif command == "negative":
    for current_number in numbers:
        if current_number < 0:
            filtered.append(current_number)
elif command == "positive":
    for current_number in numbers:
        if current_number >= 0:
            filtered.append(current_number)

print(filtered)
