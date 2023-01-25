size = int(input())

wonderland = []
alice_position = []
collected_teabags = 0

move_directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for r in range(size):
    wonderland.append(input().split())

    if 'A' in wonderland[r]:
        alice_position.append(r)
        alice_position.append(wonderland[r].index('A'))
        wonderland[r][alice_position[1]] = '*'

while collected_teabags < 10:
    direction = input()

    row = alice_position[0] + move_directions[direction][0]
    col = alice_position[1] + move_directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_position = [row, col]
    position = wonderland[row][col]
    wonderland[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        collected_teabags += int(position)

if collected_teabags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print('She did it! She went to the party.')

[print(*wonderland[row]) for row in range(size)]
