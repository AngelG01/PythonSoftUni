first_number = int(input())
second_number = int(input())
third_number = int(input())
for number1 in range(2, first_number):
    if number1 % 2 != 0:
        break
    for number2 in range(2, second_number + 1):
        
        for number3 in range(2, third_number + 1):
            if number3 % 2 != 0:
                continue
            print(f"{number1}{number2}{number3}")
