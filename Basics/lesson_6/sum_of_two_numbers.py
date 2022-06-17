start = int(input())
end = int(input())
magic_number = int(input())
count = 0
number1 = 0
number2 = 0
total = 0
not_equal = False
for number1 in range(start, end + 1):
    for number2 in range(start, end + 1):
        total = number1 + number2
        count += 1
        if total == magic_number:
            not_equal = False
            break
        else:
            not_equal = True
    if total == magic_number:
        break

if not_equal:
    print(f"{count} combinations - neither equals {magic_number}")
else:
    print(f"Combination N:{count} ({number1} + {number2} = {total})")
