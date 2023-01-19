from collections import deque

main_colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
secondary_colors = {
    "orange": {'red', 'yellow'},
    "purple": {'red', 'blue'},
    "green": {'yellow', 'blue'},
}

words = deque(input().split())
result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in main_colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                words.insert(len(words)// 2, el)

for color in set(secondary_colors.keys()).intersection(result):
    if not secondary_colors[color].issubset(result):
        result.remove(color)
print(result)