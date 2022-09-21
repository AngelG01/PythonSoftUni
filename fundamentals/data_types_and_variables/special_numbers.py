# numbers = input()
#
# for number in range(1, numbers + 1):
#     sum = 0
#     digit = number
#     for digit in range(number):
#
#         sum += number[digit]
#
#     if sum % 5 or sum % 7 or sum % 11:
#         print("True")
#     else:
#         print("False")

n = int(input())

for number in range(1, n + 1):
    sum = 0
    digits = number
    while digits > 0:
        sum += digits % 10
        digits = int(digits / 10)
