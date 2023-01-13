number_of_names = int(input())
unique_names = set()

for _ in range(number_of_names):
    unique_names.add(input())

for name in unique_names:
    print(name)


# INPUT:
# 8
# Lee
# Joey
# Lee
# Joe
# Alan
# Alan
# Peter
# Joey