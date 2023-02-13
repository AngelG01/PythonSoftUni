from collections import deque

eggs_sizes = deque(int(x) for x in input().split(', '))
papers_sizes = [int(x) for x in input().split(', ')]
boxes = 0
while len(eggs_sizes) > 0 and len(papers_sizes) > 0:

    curr_egg = eggs_sizes.popleft()

    if curr_egg == 13:
        papers_sizes[0], papers_sizes[-1] = papers_sizes[-1], papers_sizes[0]
        continue
    elif curr_egg <= 0:
        continue
    else:
        curr_paper = papers_sizes.pop()
        sum = curr_paper + curr_egg

        if sum <= 50:
            boxes += 1

if boxes > 0:
    print(f'Great! You filled {boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f'Eggs left: {", ".join(str(x) for x in eggs_sizes)}')
if papers_sizes:
    print(f'Pieces of paper left: {", ".join(str(y) for y in papers_sizes)}')
