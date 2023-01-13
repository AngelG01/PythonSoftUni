# numbers = [float(x) for x in input().split(' ') ]
# numbers_done = []
# for number in numbers:
#     count = numbers.count(number)
#     if number not in numbers_done:
#         numbers_done.append(number)
#         print(f'{number} - {count} times')

numbers = tuple(map(float, input().split(' ')))
numbers_checked = {}

for number in numbers:
    if number not in numbers_checked.keys():
        numbers_checked[number] = 0
    numbers_checked[number] += 1

[print(f'{key} - {value} times') for key, value in numbers_checked.items()]