coded_message = input().split()
decoded = []

for el in coded_message:
    char_code = ""
    word = el

    for char in el:
        if char.isdigit():
            char_code += char

    word = word.replace(char_code, chr(int(char_code)))

    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    decoded.append("".join(word))

print(' '.join(decoded))