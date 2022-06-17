floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    for room in range(0, rooms):
        total = floor * 10 + room
        # print(f"{total}", end=' ')
        if floor == floors:
            print(f"L{total}", end=' ')
        elif floor % 2 == 0:
            print(f"O{total}", end=' ')
        else:
            print(f"A{total}", end=' ')
    print()


