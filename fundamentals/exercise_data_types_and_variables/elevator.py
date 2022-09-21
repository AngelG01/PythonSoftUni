from math import ceil

people = int(input())
capacity = int(input())

courses_needed = ceil(people / capacity)
# if people % capacity != 0: courses_needed += 1

total_courses = courses_needed

print(total_courses)
