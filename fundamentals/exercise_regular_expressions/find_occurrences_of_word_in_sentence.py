import re

text = input()
key = input()

pattern = fr'\b{key}\b'
matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))

