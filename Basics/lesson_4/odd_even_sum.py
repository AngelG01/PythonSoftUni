n = int(input())
odd = 0
even = 0

for number in range(1, n + 1):
    num = int(input())
    if number % 2 == 0:
        even += num
    else:
        odd += num

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {abs(even-odd)}")
