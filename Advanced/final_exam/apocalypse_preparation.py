from collections import deque

textiles = deque(int(x) for x in input().split())
medicament = [int(y) for y in input().split()]

data = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0,
}

while textiles and medicament:
    curr_textile = textiles.popleft()
    curr_med = medicament.pop()

    total = curr_textile + curr_med

    if total == 30:
        data['Patch'] += 1
    elif total == 40:
        data['Bandage'] += 1
    elif total == 100:
        data['MedKit'] += 1
    elif total > 100:
        data['MedKit'] += 1
        diff = total - 100
        medicament[-1] += diff
    else:
        curr_med += 10
        medicament.append(curr_med)

if len(textiles) == 0 and len(medicament) == 0:
    print('Textiles and medicaments are both empty.')
elif len(textiles) == 0:
    print('Textiles are empty.')
elif len(medicament) == 0:
    print('Medicaments are empty.')

sorted_data = sorted(data.items(),
                     key=lambda x: (-x[1], x[0]))

for el, value in sorted_data:
    if value > 0:
        print(f'{el} - {value}')



if medicament:
    print(f'Medicaments left: {", ".join(str(x) for x in medicament[::-1])}')
if textiles:
    print(f'Textiles left: {", ".join(str(y) for y in textiles)}')
