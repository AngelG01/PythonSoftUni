numbers = list(map(int, input().split(', ')))
boundary = 10
while True:
    group_of_numbers = list(filter(lambda x: (x <= boundary), numbers))
    for number in group_of_numbers:
        if number in numbers:
            numbers.remove(number)
    print(f"Group of {boundary}'s: {group_of_numbers}")

    boundary += 10
    if len(numbers) == 0:
        exit()