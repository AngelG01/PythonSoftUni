numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break

    index = int(command)
    if index >= len(numbers):
        continue
    to_add = numbers[index]

    for number in range(len(numbers)):
        if numbers[number] != -1:
            if index >= len(numbers):
                break
            if numbers[number] > to_add:
                numbers[number] -= to_add
            else:
                numbers[number] += to_add

    numbers[index] = -1

shot_targets = numbers.count(-1)
numbers_as_str = list(map(str, numbers))
print(f'Shot targets: {shot_targets} -> {" ".join(numbers_as_str)}')

