number = int(input())
sum = 0
for i in range(number):
    text = input()

    value = ord(text)
    sum += value

print(f"The sum equals: {sum}")
