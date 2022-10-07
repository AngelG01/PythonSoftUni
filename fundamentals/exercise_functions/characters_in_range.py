starting_char = input()
ending_char = input()

for i in range(ord(starting_char) + 1, ord(ending_char)):
    print(chr(i), end=" ")