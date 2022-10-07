numbers = input().split()

list_of_numbers = []

for i in numbers:
    list_of_numbers.append(int(i))


# def sort(numbers: list):
#     numbers.sort()
#     return numbers


print(sorted(list_of_numbers))
