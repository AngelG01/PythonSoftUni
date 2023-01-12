stack = []

parentheses = input()
is_valid = True
for current in parentheses:
    if current == ')':
        if '(' not in stack:
            is_valid = False
            break
        if stack.pop() == '(':
            is_valid = True

    elif current == ']':
        if '[' not in stack:
            is_valid = False
            break
        if stack.pop() == '[':
            is_valid = True
    elif current == '}':
        if '{' not in stack:
            is_valid = False
            break
        if stack.pop() == '{':
            is_valid = True
    else:
        stack.append(current)

if is_valid:
    print('YES')
else:
    print('NO')
