from collections import deque

petrol_pumps_number = int(input())

stations = deque()

for _ in range(petrol_pumps_number):
    info = tuple(map(int, input().split()))
    stations.append(info)

for i in range(len(stations)):
    index = i
    counter = 0
    tank = 0
    for pump in stations:
        fuel, distance = pump
        if tank + fuel < distance:
            stations.append(stations.popleft())
            break
        else:
            tank += fuel - distance
            counter += 1

    if counter == petrol_pumps_number:
        print(index)
        break


