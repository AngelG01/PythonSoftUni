countries= input().split(', ')
capitals = input().split(', ')

combined = zip(countries, capitals)
for country, capital in combined:
    print(f'{country} -> {capital}')
