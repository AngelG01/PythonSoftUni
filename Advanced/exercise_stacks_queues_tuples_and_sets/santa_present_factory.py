from collections import deque

materials_for_toys = deque(int(x) for x in input().split())
magic_level = deque(int(y) for y in input().split())

possible_toys = [150, 250, 300, 400]
toys_made = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0,

}

while materials_for_toys and magic_level:
    current_material = materials_for_toys.pop()
    current_magic = magic_level.popleft()
    result = current_material * current_magic

    if current_magic == 0:
        materials_for_toys.append(current_material)
        continue

    if current_material == 0:
        magic_level.appendleft(current_magic)
        continue

    if result in possible_toys:
        if result == 150:
            toys_made['Doll'] += 1
        elif result == 250:
            toys_made['Wooden train'] += 1
        elif result == 300:
            toys_made['Teddy bear'] += 1
        else:
            toys_made['Bicycle'] += 1

    elif result < 0:
        new_value = current_material + current_magic
        materials_for_toys.append(new_value)
    elif result > 0:
        new_material = current_material + 15
        materials_for_toys.append(new_material)



if toys_made['Doll'] > 0 and toys_made['Wooden train'] > 0 or toys_made['Teddy bear'] > 0 and toys_made['Bicycle'] > 0:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_for_toys:
    print(
        f'Materials left: {", ".join([str(x) for x in materials_for_toys][::-1])}')

if magic_level:
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')

sorted_toys = dict(sorted(toys_made.items()))

for key, value in sorted_toys.items():
    if value != 0:
        print(f'{key}: {value}')

# INPUT:
#
# 30 5 15 60 0 30
# -15 10 5 -15 25
#
# -------------------
#
# 10 -5 20 15 -30 10
# 40 60 10 4 10 0
#
# -------------------
#
# 30 10
# 15 10 5 0 10
