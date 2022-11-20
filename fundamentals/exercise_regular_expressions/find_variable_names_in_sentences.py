import re

text = input()
numbers = []

pattern = r'\b_[a-zA-Z0-9]*\b'
matches = re.findall(pattern, text)

for match in matches:
    numbers.append(match.replace('_', ''))
print(','.join(numbers))
