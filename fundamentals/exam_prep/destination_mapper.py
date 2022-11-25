import re

text = input()
points = 0
destinations = []
pattern = r'[=][A-Z][a-zA-Z]{2,}[=]|[\/][A-Z][a-zA-Z]{2,}[\/]'
matches = re.findall(pattern, text)

for match in matches:
    if '=' in match:
        destination = match.replace('=', '')
        destinations.append(destination)
    else:
        destination = match.replace('/', '')
        destinations.append(destination)

    points += (len(match) - 2)
if destinations:
    print(f'Destinations: {", ".join(destinations)}')
else:
    print('Destinations: ')
print(f'Travel Points: {points}')
