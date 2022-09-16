divisor = int(input())
boundary = int(input())

for number in range(boundary, 0, -1):
    max = number / divisor

    if max.is_integer():
        print(number)
        break
