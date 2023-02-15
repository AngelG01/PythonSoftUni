from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:

    curr_bowl = bowls_of_ramen.pop()
    curr_customer = customers.popleft()

    if curr_bowl == curr_customer:
        pass
    elif curr_bowl > curr_customer:
        diff = curr_bowl - curr_customer
        bowls_of_ramen.append(diff)
    elif curr_bowl < curr_customer:
        diff = curr_customer - curr_bowl
        customers.appendleft(diff)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(str(y) for y in customers)}')