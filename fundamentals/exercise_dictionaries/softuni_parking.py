number_of_people = int(input())
parking_lot = {}

for n in range(number_of_people):
    command = input().split(' ')

    if command[0] == 'register':
        username, license_plate = command[1], command[2]
        if username not in parking_lot.keys():
            # if len(parking_lot) == 1:
            #     break
            parking_lot[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate}')
    elif command[0] == 'unregister':
        username = command[1]
        if username not in parking_lot.keys():
            print(f'ERROR: user {username} not found')
        else:
            del parking_lot[username]
            print(f'{username} unregistered successfully')

for key, value in parking_lot.items():
    print(f'{key} => {value}')

