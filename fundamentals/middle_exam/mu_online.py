rooms = input().split('|')
health = 100
bitcoins = 0
for curr_room in rooms:
    current_room = curr_room.split()

    if current_room[0] == 'potion':

        check_health = health + int(current_room[1])
        if health < 100:
            if check_health < 100:
                health += int(current_room[1])
                print(f'You healed for {current_room[1]} hp.')
                print(f'Current health: {health} hp.')
            else:
                needed_health = 100 - health
                print(f'You healed for {needed_health} hp.')
                health = 100
                print(f'Current health: {health} hp.')

    elif current_room[0] == 'chest':
        bitcoins += int(current_room[1])
        print(f'You found {current_room[1]} bitcoins.')

    else:
        health -= int(current_room[1])
        if health > 0:
            print(f'You slayed {current_room[0]}.')
        else:
            print(f'You died! Killed by {current_room[0]}.')
            print(f'Best room: {rooms.index(curr_room) + 1}')
            exit()

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
