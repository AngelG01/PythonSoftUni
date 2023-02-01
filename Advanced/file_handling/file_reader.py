file = open('numbers.txt', 'r')
sum = 0
for el in file:
    sum += int(el)
print(sum)
