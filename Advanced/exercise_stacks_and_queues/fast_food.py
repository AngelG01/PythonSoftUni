from collections import deque

food_quantity = int(input())
orders_queue = input().split()

orders_as_int = [int(order) for order in orders_queue]
print(max(orders_as_int))
queue = deque(orders_as_int)

while len(queue) > 0:
    order = queue[0]
    if food_quantity >= order:
        food_quantity -= order
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print('Orders complete')
else:
    print(f'Orders left: ', end='')
    for element in queue:
        print(element, end=' ')
