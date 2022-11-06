word = input()
occurrences = {}
for letter in word:
    if letter == ' ':
        continue
    if letter not in occurrences.keys():
        occurrences[letter] = 0
    occurrences[letter] += 1

for char, count in occurrences.items():
    print(f'{char} -> {count}')
