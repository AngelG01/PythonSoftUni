sequence = input().split()
rack_capacity = int(input())
packs = [int(pack) for pack in sequence]
total_current = 0
racks_count = 0
for current in range(len(packs) - 1, -1, -1):

    if total_current + packs[current] < rack_capacity:
        total_current += packs[current]
    elif total_current + packs[current] == rack_capacity:
        racks_count += 1
        total_current = 0
    elif total_current + packs[current] > rack_capacity:
        racks_count += 1
        total_current = 0
        total_current += packs[current]
    if current == 0 and total_current > 0:
        racks_count += 1

print(racks_count)
