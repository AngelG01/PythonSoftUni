message = input()

command = input().split('|')

while command[0] != 'Decode':

    if command[0] == 'Move':
        count = int(command[1])
        letters = message[:count]
        message = message.replace(letters, '')
        message += letters
    elif command[0] == 'Insert':
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif command[0] == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)
    command = input().split('|')
print(f'The decrypted message is: {message}')

