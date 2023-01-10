numbers = input().split()

for element in range(len(numbers) - 1, -1, -1):
    print(numbers.pop(), end=' ')
