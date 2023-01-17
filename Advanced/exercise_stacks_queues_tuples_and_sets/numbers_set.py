first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

count_of_commands = int(input())

for _ in range(count_of_commands):
    first_command, *data = input().split()

    command = first_command + ' ' + data.pop(0)

    if command == 'Add First':
        [first_sequence.add(int(x)) for x in data]
    elif command == 'Add Second':
        [second_sequence.add(int(y)) for y in data]
    elif command == 'Remove First':
        [first_sequence.discard(int(x)) for x in data]
    elif command == 'Remove Second':
        [second_sequence.discard(int(y)) for y in data]
    elif command == 'Check Subset':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print(True)
        else:
            print(False)

first_sort_1 = sorted(first_sequence)
second_sort_2 = sorted(second_sequence)

print(*first_sort_1, sep=', ')
print(*second_sort_2, sep=', ')

# INPUT:
# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
# ________________________
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
