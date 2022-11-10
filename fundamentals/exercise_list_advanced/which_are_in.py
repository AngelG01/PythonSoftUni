key_words = input().split(', ')
words_to_check = input().split(', ')

logged = []
for word in key_words:
    for curr in words_to_check:
        if word in curr:
            logged.append(word)
            break
print(logged)

