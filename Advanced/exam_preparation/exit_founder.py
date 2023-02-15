players = input().split(', ')

matrix = []

for r in range(6):
    column = input().split()
    matrix.append(column)

first_player_needs_rest = False
second_player_needs_rest = False

while True:
    first_player_position = input().strip('(').strip(')').split(', ')

    if not first_player_needs_rest:
        row, col = int(first_player_position[0]), int(first_player_position[1])

        position = matrix[row][col]

        if position == 'E':
            print(f"{players[0]} found the Exit and wins the game!")
            break
        elif position == 'T':
            print(f'{players[0]} is out of the game! The winner is {players[1]}.')
            break
        elif position == 'W':
            print(f"{players[0]} hits a wall and needs to rest.")
            first_player_needs_rest = True
    else:
        first_player_needs_rest = False

    second_player_position = input().strip('(').strip(')').split(', ')

    if not second_player_needs_rest:
        row, col = int(second_player_position[0]), int(second_player_position[1])

        position = matrix[row][col]

        if position == 'E':
            print(f"{players[1]} found the Exit and wins the game!")
            break
        elif position == 'T':
            print(f'{players[1]} is out of the game! The winner is {players[0]}.')
            break
        elif position == 'W':
            print(f"{players[1]} hits a wall and needs to rest.")
            second_player_needs_rest = True
    else:
        second_player_needs_rest = False
