import re

text = input()
numebrs = []
while text:
    pattern = r'\d+'
    matches = re.findall(pattern, text)
    if matches:
        numebrs.extend(matches)
    text = input()

for current in numebrs:
    print(current, end=' ')