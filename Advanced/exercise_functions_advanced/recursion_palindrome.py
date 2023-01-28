def palindrome(word, n):
    if n != 0:
        return palindrome(word, n + 1)
    else:
        if word == word[::-1]:
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
