message = input()
command = input().split(':|:')

while command[0] != 'Reveal':
    if command[0] == 'InsertSpace':
        index = int(command[1])
        s = message[:index] + ' ' + message[index:]
        message = s
        print(message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            message += substring[::-1]
            print(message)
        else:
            print('error')

    elif command[0] == 'ChangeAll':
        substring = command[1]
        letter = command[2]
        replaced = message.replace(substring, letter)
        message = replaced
        print(message)
    command = input().split(':|:')
print(f'You have a new text message: {message}')
