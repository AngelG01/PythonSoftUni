text = input()

letters = {}

for letter in text:
    if letter not in letters.keys():
        letters[letter] = 0
    letters[letter] = text.count(letter)

myKeys = list(letters.keys())
myKeys.sort()
sorted_dict = {i: letters[i] for i in myKeys}

for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')

# INPUT:
# SoftUni rocks