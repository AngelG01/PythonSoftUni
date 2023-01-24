lists = input().split('|')
flattened = []
for element in lists[::-1]:
    flattened.extend(element.split())


print(*flattened)

