year = int(input()) + 1

distinct_digit = False

while not distinct_digit:
    digits = []
    for elem in str(year):
        digits.append(elem)

    if len(digits) == len(set(digits)):
        distinct_digit = True
        break
    year += 1
print(year)

# year = int(input()) + 1
#
# while len(set(str(year))) != len(str(year)):
#     year += 1
#
# print(year)