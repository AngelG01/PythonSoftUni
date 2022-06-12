name_of_actor = input()
points = float(input())
count_of_evaluators = int(input())

total_points = points
for count in range(0, count_of_evaluators):
    evaluator_name = input()
    points_of_evaluator = float(input())
    evaluators = 0
    for letter_count in evaluator_name:
        evaluators += 1

    total_points += ((evaluators * points_of_evaluator) / 2)

    if total_points > 1250.5:
        break

not_enough = 1250.5 - total_points

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {name_of_actor} you need {not_enough:.1f} more!")
