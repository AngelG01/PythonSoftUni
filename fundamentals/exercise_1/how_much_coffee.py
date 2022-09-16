command = input()
coffee_count = 0

while command != "END":
    if command == "coding" or command == "CODING":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    elif command == "cat" or command == "CAT":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    elif command == "dog" or command == "DOG":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    elif command == "movie" or command == "MOVIE":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2

    command = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)