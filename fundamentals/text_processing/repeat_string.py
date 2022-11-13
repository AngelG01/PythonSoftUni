words = input().split()

for current_word in words:
    for i in range(len(current_word)):
        print(current_word, end='')