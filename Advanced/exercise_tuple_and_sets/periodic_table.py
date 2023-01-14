unique_elements = set()
for _ in range(int(input())):
    elements = input().split()
    for element in elements:
        unique_elements.add(element)

[print(element) for element in unique_elements]

# INPUT:
# 4
# Ce O
# Mo O Ce
# Ee
# Mo
