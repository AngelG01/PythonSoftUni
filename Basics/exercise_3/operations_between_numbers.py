number_1 = int(input())
number_2 = int(input())
operation = input()
result = 0
even_or_odd = ""

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    if number_2 != 0:
        result = number_1 / number_2
elif operation == "%":
    if number_2 != 0:
        result = number_1 % number_2


if operation == "+" or operation == "-" or operation == "*":
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{number_1} {operation} {number_2} = {result} - {even_or_odd}")
elif operation == "/":
    if number_2 != 0:
        print(f"{number_1} {operation} {number_2} = {result:.2f}")
    else:
        print(f"Cannot divide {number_1:.0f} by zero")
elif operation == "%":
    if number_2 != 0:
        print(f"{number_1} {operation} {number_2} = {result}")
    else:
        print(f"Cannot divide {number_1} by zero")
