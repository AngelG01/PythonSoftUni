numbers = input().split()
list_numbers = []

for i in numbers:
    list_numbers.append(int(i))

print(f'The minimum number is {min(list_numbers)}')
print(f'The maximum number is {max(list_numbers)}')
print(f'The sum number is: {sum(list_numbers)}')


