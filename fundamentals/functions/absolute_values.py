text = input().split()
numbers_as_int = []

for number in text:
    numbers_as_int.append(float(number))


def absolute_value():
    absolute_number = []
    for current_number in numbers_as_int:
        absolute_number.append(abs(current_number))

    print(absolute_number)


absolute_value()
