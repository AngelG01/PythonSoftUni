from collections import  deque
queue = deque(['Eric', 'John', 'Michael'])
print(queue)
queue.append('Angel')
print(queue)
queue.popleft()
print(queue)