counts = int(input())

for i in range(0, counts + 1):
    for j in range(0, i):
        print("*", end="")

    print("")
for k in range(counts-1, 0, -1):
    for l in range(0, k):
        print("*", end="")

    print("")