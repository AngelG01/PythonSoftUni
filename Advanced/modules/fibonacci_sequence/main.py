from fibonacci_creator import *

command = input().split()
fibonacci_sequence = []

while command[0] != 'Stop':

    if command[0] == 'Create':
        count = command[2]
        fibonacci_sequence = fibonacci(count)
        [print(x, end=' ') for x in fibonacci_sequence]
        print()

    elif command[0] == 'Locate':
        number = int(command[1])

        if number in fibonacci_sequence:
            index = fibonacci_sequence.index(number)
            print(f'The number - {number} is at index {index}')

        else:
            print(f'The number {number} is not in the sequence')

    command = input().split()
