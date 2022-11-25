nuber_of_pieces = int(input())
data = {}
for _ in range(nuber_of_pieces):
    info = input().split('|')
    piece, composer, key = info
    data[piece] = [composer, key]

command = input().split('|')
while command[0] != 'Stop':

    current_command = command[0]

    if current_command == 'Add':
        piece, composer, key = command[1:]
        if piece not in data.keys():
            data[piece] = [composer, key]
            print(f'{piece} by {composer} in {key} added to the collection!')
        else:
            print(f'{piece} is already in the collection!')

    elif current_command == 'Remove':
        piece = command[1]
        if piece in data.keys():
            del data[piece]
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif current_command == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        if piece in data.keys():
            data[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    command = input().split('|')

sorted_data = sorted(data.keys(), key=lambda x: x.lower())
for current, element in data.items():
    print(f'{current} -> Composer: {element[0]}, Key: {element[1]}')
