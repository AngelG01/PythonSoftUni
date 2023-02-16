from collections import deque

total_energy = 0
toys_made = 0
counter = 1
energy = deque(int(x) for x in input().split())
materials = [int(y) for y in input().split()]

while energy and materials:
    curr_elf = energy.popleft()
    curr_material = materials.pop()
    if curr_elf < 5:
        materials.append(curr_material)
        continue
    if curr_elf >= curr_material:
        if counter % 5 == 0:
            if counter % 3 == 0:
                diff = curr_elf - (2 * curr_material)
            else:
                diff = curr_elf - curr_material
            if diff >= 0:
                if counter % 3 == 0:
                    total_energy += (2 * curr_material)
                    energy.append(diff)
                else:
                    total_energy += curr_material
                    energy.append(diff)
            else:
                curr_elf *= 2
                energy.append(curr_elf)
        elif counter % 3 == 0:
            diff = curr_elf - (2 * curr_material)
            if diff >= 0:
                energy.append(diff + 1)
                toys_made += 2
                total_energy += (2 * curr_material)
            else:
                materials.append(curr_material)
                curr_elf *= 2
                energy.append(curr_elf)


        else:
            diff = (curr_elf - curr_material) + 1
            energy.append(diff)
            toys_made += 1
            total_energy += curr_material
    else:
        curr_elf *= 2
        energy.append(curr_elf)
        materials.append(curr_material)

    counter += 1

print(f'Toys: {toys_made}')
print(f'Energy: {total_energy}')
if energy:
    print(f'Elves left: {", ".join(str(x) for x in energy)}')
if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')
