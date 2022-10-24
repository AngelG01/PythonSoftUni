friends = input().split(', ')
alter_friends = friends.copy()
command = input().split()
blacklisted = []
lost = []

while True:

    if command[0] == 'Blacklist':
        if command[1] in friends:
            index = friends.index(command[1])
            blacklisted.append(command[1])
            friends[index] = 'Blacklisted'
            print(f'{command[1]} was blacklisted.')
        else:
            print(f'{command[1]} was not found.')
    elif command[0] == 'Error':
        index = int(command[1])

        if 0 <= index < len(friends) and alter_friends[index] not in blacklisted and alter_friends[index] not in lost:
            lost.append(friends[index])
            print(f"{friends[index]} was lost due to an error.")
            friends[index] = 'Lost'
        else:
            command = input().split()
            continue
    elif command[0] == 'Change':
        index = int(command[1])
        new_name = command[2]

        if 0 <= index < len(friends):
            current_name = friends[index]
            friends[index] = new_name
            print(f'{current_name} changed his username to {new_name}.')

    if command[0] == 'Report':
        break

    command = input().split()

print(f'Blacklisted names: {len(blacklisted)}')
print(f'Lost names: {len(lost)}')
print(' '.join(friends))
