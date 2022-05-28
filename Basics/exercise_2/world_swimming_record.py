from math import floor

world_record = float(input())
distance = float(input())
time_per_meter = float(input())

time = distance * time_per_meter
added_time = floor(distance / 15) * 12.5

total_time = time + added_time

if total_time >= world_record:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
