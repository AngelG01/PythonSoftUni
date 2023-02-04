from collections import deque

daily_food = [int(x) for x in input().split(', ')]
daily_stamina = deque(int(x) for x in input().split(', '))

mountains = [
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
]
conquered_peaks = []
peak_tracker = 0

for curr_day in range(7):
    curr_food = daily_food.pop()
    curr_stamina = daily_stamina.popleft()

    curr_effort = curr_food + curr_stamina
    needed_effort = mountains[peak_tracker][1]

    if curr_effort >= needed_effort:
        conquered_peaks.append(mountains[peak_tracker][0])
        peak_tracker += 1

    if peak_tracker == 5:
        break

if len(conquered_peaks) == 5:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print('Conquered peaks:')
    print('\n'.join(conquered_peaks))
