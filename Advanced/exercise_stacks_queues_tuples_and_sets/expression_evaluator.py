# expression = input().split()
#
# numbers = []
# total = 0
#
# for element in expression:
#
#     if len(element) == 1:
#         if element.isdigit():
#             numbers.append(int(element))
#             continue
#     else:
#         if element[1].isdigit():
#             numbers.append(int(element))
#             continue
#
#     if element == '+':
#         for el in numbers:
#             total += el
#         numbers.clear()
#     elif element == '-':
#         if total == 0 and len(numbers) > 1:
#             total = numbers[0]
#             for el in range(1, len(numbers)):
#                 total -= numbers[el]
#         else:
#             for el in numbers:
#                 total -= el
#
#         numbers.clear()
#     elif element == '*':
#         if total == 0 and len(numbers) > 1:
#             total = numbers[0]
#             for el in range(1, len(numbers)):
#                 total *= numbers[el]
#         else:
#             for el in numbers:
#                 total *= el
#
#         numbers.clear()
#     elif element == '/':
#         for el in numbers:
#             total /= el
#         total = int(total)
#         numbers.clear()
# print(int(total))
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