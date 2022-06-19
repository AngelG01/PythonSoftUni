first_number = int(input())
second_number = int(input())
third_number = int(input())

for number1 in range(2, first_number + 1, 2):
    for number2 in range(2, second_number + 1):
        for number3 in range(2, third_number + 1, 2):
            if number2 == 2 or number2 == 3 or number2 == 5 or number2 == 7:
                print(f"{number1} {number2} {number3}")
