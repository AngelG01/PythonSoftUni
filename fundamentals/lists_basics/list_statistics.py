rotations = int(input())
positive_numbers = []
negative_numbers = []
sum_negative = 0
for i in range(rotations):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
       
    else:
        negative_numbers.append(number)
        sum_negative += number

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum_negative}")
