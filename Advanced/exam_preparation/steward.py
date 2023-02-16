from collections import deque

seats = input().split(', ')

first_seq = deque(int(x) for x in input().split(', '))
second_seq = deque(int(x) for x in input().split(', '))

rotations = 0
matched_seats = []

while rotations != 10 and len(matched_seats) < 3:
    curr_one = first_seq.popleft()
    curr_two = second_seq.pop()

    letter = chr(curr_one + curr_two)

    combination_A = f'{curr_one}{letter}'
    combination_B = f'{curr_two}{letter}'

    if combination_A in seats:
        if combination_A not in matched_seats:
            matched_seats.append(combination_A)
    elif combination_B in seats:
        if combination_B not in matched_seats:
            matched_seats.append(combination_B)
    else:
        first_seq.append(curr_one)
        second_seq.appendleft(curr_two)

    rotations += 1
print(f'Seat matches: {", ".join(matched_seats)}')
print(f'Rotations count: {rotations}')
