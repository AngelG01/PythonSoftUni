journal = input().split(', ')
command = input().split(' - ')

while command[0] != 'Craft!':

    if command[0] == 'Collect':
        if not command[1] in journal:
            journal.append(command[1])

    elif command[0] == 'Drop':
        if command[1] in journal:
            journal.remove(command[1])
    elif command[0] == 'Combine Items':
        items = command[1].split(':')
        old_item = items[0]
        new_item = items[1]
        if old_item in journal:
            index = journal.index(old_item) + 1
            journal.insert(index, new_item)
    elif command[0] == 'Renew':
        if command[1] in journal:
            journal.remove(command[1])
            journal.append(command[1])

    command = input().split(' - ')

print(', '.join(journal))
