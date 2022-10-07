numbers = input().split(', ')


def palindrome(number):
    for number in numbers:
        reversed_number = number[::-1]
        if number == reversed_number:
            print('True')
        else:
            print('False')
    return ""


print(palindrome(numbers))
