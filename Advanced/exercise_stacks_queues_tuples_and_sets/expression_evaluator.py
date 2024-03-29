from functools import reduce

expression = input().split()

functions = {

    '+': lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    '*': lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    '-': lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
    '/': lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
}
index = 0

while index < len(expression):
    element = expression[index]
    if element in '+*/-':
        result = functions[element](index)
        [expression.pop(1) for i in range(index)]
        expression[0] = result
        index = 0
    index += 1
print(int(*expression))


# INPUT:
# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
