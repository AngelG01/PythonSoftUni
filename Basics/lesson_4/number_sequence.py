n = int(input())

max_number = 0
min_number = 0

for number in range(0, n):
    i = int(input())
    if i >= max_number:
        max_number = i
    elif i <= min_number:
        min_number = i

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")

