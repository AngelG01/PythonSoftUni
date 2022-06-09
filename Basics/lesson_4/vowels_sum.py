text = input()

value = 0
total = 0

for letter in text:
    if letter == "a":
        value = 1
        total += value
    elif letter == "e":
        value = 2
        total += value
    elif letter == "i":
        value = 3
        total += value
    elif letter == "o":
        value = 4
        total += value
    elif letter == "u":
        value = 5
        total += value


print(total)