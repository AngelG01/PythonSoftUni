lines = int(input())
parking_lot = set()
for n in range(lines):
    info = tuple(input().split(', '))

    direction, plate_number = info

    if direction == 'IN':
        parking_lot.add(plate_number)
    elif direction == 'OUT':
        if plate_number in parking_lot:
            parking_lot.remove(plate_number)

if parking_lot:
    [print(f'{car}') for car in parking_lot]
else:
    print('Parking Lot is Empty')


# INPUT:
# 10
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# IN, CA9999TT
# IN, CA2866HI
# OUT, CA1234TA
# IN, CA2844AA
# OUT, CA2866HI
# IN, CA9876HH
# IN, CA2822UU
#
# ________________
#
# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA