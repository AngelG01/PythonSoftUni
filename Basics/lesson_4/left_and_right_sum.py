n = int(input())

left = 0
right = 0

for number in range(1, n + 1):
    i = int(input())
    left += i

for number in range(1, n + 1):
    i = int(input())
    right += i

if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(right - left)}")
   