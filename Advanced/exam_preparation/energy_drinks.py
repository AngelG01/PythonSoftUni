from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque(int(x) for x in input().split(', '))
total_caffeine = 0

while len(caffeine) and len(energy_drinks):
    curr_caffeine = caffeine.pop()
    curr_drink = energy_drinks.popleft()
    total = curr_caffeine * curr_drink

    if total_caffeine + total <= 300:
        total_caffeine += total
    else:
        energy_drinks.append(curr_drink)
        diff = total_caffeine - 30
        if diff >= 0:
            total_caffeine -= 30
        else:
            total_caffeine = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')
