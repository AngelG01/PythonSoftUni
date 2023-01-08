expression = input()
parentheses = []
for element in range(len(expression)):
    if expression[element] == '(':
        parentheses.append(element)
    elif expression[element] == ')':
        start_index = parentheses.pop()
        print(expression[start_index:element + 1])
