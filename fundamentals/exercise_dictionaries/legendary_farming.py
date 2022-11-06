matrix = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
obtained = False
while not obtained:
    materials = input().split(' ')

    for i in range(0, len(materials), 2):
        count = int(materials[i])
        material = materials[i + 1].lower()
        if material == 'shards' or material == 'fragments' or material == 'motes':
            matrix[material] += count
            if matrix[material] >= 250:
                matrix[material] -= 250
                if material == 'shards':
                    print('Shadowmourne obtained!')
                elif material == 'fragments':
                    print('Valanyr obtained!')
                else:
                    print('Dragonwrath obtained!')
                obtained = True
                break

        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += count


for mater, value in matrix.items():
    print(f'{mater}: {value}')
for element, count in junk.items():
    print(f'{element}: {count}')

