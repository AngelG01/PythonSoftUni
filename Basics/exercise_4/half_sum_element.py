import sys

n = int(input())

max_num = -sys.maxsize
total = 0

for i in range(1, n + 1):
    current_num = int(input())
    total += current_num

    if current_num > max_num:
        max_num = current_num

final_total = total - max_num
diff = abs(final_total - max_num)
if final_total == max_num:
    print("Yes")
    print(f"Sum = {final_total}")
else:
    print("No")
    print(f"Diff = {diff}")


