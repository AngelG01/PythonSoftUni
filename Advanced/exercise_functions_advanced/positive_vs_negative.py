positive_numbers = 0
negative_numbers = 0

numbers = [int(x) for x in input().split()]

for number in numbers:

    if number > 0:
        positive_numbers += number
    else:
        negative_numbers += number



print(negative_numbers)
print(positive_numbers)

if abs(negative_numbers) > positive_numbers:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')
