number_of_rooms = int(input())
left_chairs = 0
total_chairs = 0
visitors = 0
for room in range(1, number_of_rooms + 1):
    room_info = input().split()
    difference = len(room_info[0]) - int(room_info[1])
    total_chairs += len(room_info[0])
    visitors += int(room_info[1])

    if difference < 0:
        chairs_needed = int(room_info[1]) - len(room_info[0])
        print(f'{abs(chairs_needed)} more chairs needed in room {room}')
    else:
        left_chairs += difference


if total_chairs >= visitors:
    print(f'Game On, {left_chairs} free chairs left')

