operation = input()
first_number = int(input())
second_number = int(input())


def calculations(operation, first_number, second_number):
    result = 0
    if operation == "multiply":
        result = first_number * second_number
    elif operation == "divide":
        result = int(first_number / second_number)
    elif operation == "add":
        result = first_number + second_number
    elif operation == "subtract":
        result = first_number - second_number
    return result


print(calculations(operation, first_number, second_number))
