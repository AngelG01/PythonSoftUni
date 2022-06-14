width = int(input())
length = int(input())
height = int(input())

total_room_space = width * length * height
box_space = 0

command = input()
while total_room_space >= box_space:
    if command != "Done":
        boxes = int(command)
        box_space += boxes
    else:
        break

    if box_space <= total_room_space:
        command = input()

enough = total_room_space - box_space
not_enough = box_space - total_room_space

if box_space > total_room_space:
    print(f"No more free space! You need {not_enough} Cubic meters more.")
else:
    print(f"{enough} Cubic meters left.")
