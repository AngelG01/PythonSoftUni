materials = {}

while True:
    key = input()
    if key == 'stop':
        break
    value = int(input())

    if key not in materials.keys():
        materials[key] = value
    else:
        materials[key] += value

for material, value in materials.items():
    print(f'{material} -> {value}')
