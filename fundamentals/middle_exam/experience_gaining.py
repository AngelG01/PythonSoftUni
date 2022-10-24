needed_experience = int(input())
count_of_battles = int(input())
collected_experience = 0
counter = 0

for current_battle in range(1, count_of_battles + 1):

    if collected_experience >= needed_experience:
        break

    counter += 1
    experience = int(input())

    if current_battle % 3 == 0:
        experience += (experience * 0.15)

    if current_battle % 5 == 0:
        experience -= (experience * 0.10)

    if current_battle % 15 == 0:
        experience += (experience * 0.05)

    collected_experience += experience

difference = needed_experience - collected_experience
if collected_experience >= needed_experience:
    print(f'Player successfully collected his needed experience for {counter} battles.')
else:
    print(f'Player was not able to collect the needed experience, {difference:.2f} more needed.')