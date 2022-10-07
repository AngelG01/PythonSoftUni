# numbers = [int(number) for number in input().split()]
# top_numbers = int(input())
# top = []
#
# numbers.sort()
#
# for numb in range(1, top_numbers + 1):
#     top.append(numbers[-numb])
#
# list_string = map(str, top)
#
# print(", ".join(list_string))


numbers = [int(number) for number in input().split()]
top_numbers = int(input())

for number in range(top_numbers):
    for element in numbers:
        if min(numbers) == element:
            numbers.remove(element)
            break


for number in range(len(numbers)):
    if numbers.index(numbers[number]) != len(numbers) - 1:
        print(f"{numbers[number]}, ", end="")
    else:
        print(f"{numbers[number]}", end="")

