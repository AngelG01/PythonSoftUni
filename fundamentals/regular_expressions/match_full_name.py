import re

name = input()
pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'
matches = re.findall(pattern, name)

print(' '.join(matches))

