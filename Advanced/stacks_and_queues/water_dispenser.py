from collections import deque

liters_of_water = int(input())
queue = deque()
command = input()

while command != 'Start':
    queue.append(command)
    command = input()

operation = input().split()
while operation[0] != 'End':

    if operation[0].isdigit():
        water_needed = int(operation[0])
        if water_needed <= liters_of_water:
            liters_of_water -= water_needed
            print(f'{queue.popleft()} got water')
        else:
            print(f'{queue.popleft()} must wait')
    else:
        liters_of_water += int(operation[1])
    operation = input().split()
print(f'{liters_of_water} liters left')



