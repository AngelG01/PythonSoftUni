from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

functions = {

    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

total_honey = 0

while nectar and working_bees:

    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        working_bees.appendleft(current_bee)
    elif current_nectar > current_bee:
        symbol = symbols.popleft()
        result = functions[symbol](current_bee, current_nectar)
        total_honey += abs(result)

print(f'Total honey made: {total_honey}')
if working_bees:
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')
if nectar:
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')


# INPUT:
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /

