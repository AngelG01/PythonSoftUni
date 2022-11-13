key_words = input().split(', ')
text = input()

for key in key_words:
    while key in text:
        text = text.replace(key, '*' * len(key))
print(text)