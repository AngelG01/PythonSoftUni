import re

text = input()
pattern = r'([@|#])[a-zA-Z]{3,}\1\1[a-zA-Z]{3,}\1'
matches = re.finditer(pattern, text)
reversed_count = 0
valid = 0
mirror_words = []
for match in matches:
    words = ''
    word1 = ''
    word2 = ''
    if '@' in match.group(0):
        words = (match.group(0).split('@'))
    else:
        words = (match.group(0).split('#'))

    for word in range(1, len(words), 2):
        word1 = words[word]
        word2 = words[word + 2]
        break

    if word1 == word2[::-1]:

        mirror_words.append(word1)
        mirror_words.append(word2)
        valid += 1
    else:
        valid += 1

if valid != 0:
    print(f'{valid} word pairs found!')
else:
    print('No word pairs found!')
if len(mirror_words) == 0:
    print('No mirror words!')
else:
    print('The mirror words are: ')
    for current in range(0, len(mirror_words), 2):
        if current == len(mirror_words) - 2:
            print(f'{mirror_words[current]} <=> {mirror_words[current + 1]}')
        else:
            print(f'{mirror_words[current]} <=> {mirror_words[current + 1]}', end=', ')
