text = list(input())
reversed = []

for letter in range(len(text)):
    reversed.append(text.pop())

print(''.join(reversed))