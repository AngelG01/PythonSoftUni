commands_count = int(input())
stack = []

for n in range(commands_count):
    command = input().split()

    if command[0] == '1':
        stack.append(int(command[1]))
    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
    elif command[0] == '3':
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == '4':
        if len(stack) > 0:
            print(min(stack))

for number in range(len(stack) - 1, 0, -1):
    print(f'{stack[number]}, ', end='')
print(stack[0])
