all_stops = input()

command = input().split(':')

while command[0] != 'Travel':

    if command[0] == 'Add Stop':
        index = int(command[1])
        place = command[2]

        if index in range(len(all_stops)):
            all_stops = all_stops[:index] + place + all_stops[index:]
        print(all_stops)
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(all_stops)) and end_index in range(len(all_stops)):
            all_stops = all_stops[:start_index] + all_stops[end_index + 1:]
        print(all_stops)

    elif command[0] == 'Switch':
        old_place = command[1]
        new_place = command[2]
        if old_place in all_stops:
            all_stops = all_stops.replace(old_place, new_place)
        print(all_stops)

    command = input().split(':')
print(f'Ready for world tour! Planned stops: {all_stops}')
