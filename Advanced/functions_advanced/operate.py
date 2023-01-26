import functools


def operate(operator, *args):
    numbers = args

    if operator == '+':
        return functools.reduce(lambda a, b: a + b, numbers)

    elif operator == '-':
        return functools.reduce(lambda a, b: a - b, numbers)
    elif operator == '*':
        return functools.reduce(lambda a, b: a * b, numbers)
    elif operator == '/':
        return functools.reduce(lambda a, b: a / b, numbers)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 50, 4, 3))
