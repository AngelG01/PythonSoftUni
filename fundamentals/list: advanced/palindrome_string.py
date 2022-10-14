text = input().split()
searched_palindrome = input()
list_of_palindrome = []
count = 0
# count_of_palindrome = [', '.join([word for word in text if word == ''.join(reversed(word))])]
for word in text:
    if word == searched_palindrome:
        count = text.count(searched_palindrome)
    if word == word[::-1]:
        list_of_palindrome.append(word)

print(list_of_palindrome)
print(f'Found palindrome {count} times')
