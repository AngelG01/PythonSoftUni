password = input()


def length(password):
    if len(password) >= 6:
        return True
    return False


def valid_char(password):
    check = password.isalnum()
    if check:
        return True
    return False


def digits_count(password):
    count = 0
    for char in password:
        if char.isdigit():
            count += 1

    if count >= 2:
        return True
    return False


if length(password) and valid_char(password) and digits_count(password):
    print('Password is valid')

if not length(password):
    print('Password must be between 6 and 10 characters')
if not valid_char(password):
    print('Password must consist only of letters and digits')
if not digits_count(password):
    print('Password must have at least 2 digits')