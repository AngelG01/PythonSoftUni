number_of_length = input().split()
f_count = int(number_of_length[0])
s_count = int(number_of_length[1])
first_set = set()
second_set = set()

for _ in range(f_count):
    numb = input()
    first_set.add(numb)
for _ in range(s_count):
    number = input()
    second_set.add(number)

for current in first_set:
    if current in second_set:
        print(current)

# INPUT:
# 2 2
# 1
# 3
# 1
# 5

