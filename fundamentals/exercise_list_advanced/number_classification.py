numbers = list(map(int, input().split(', ')))

positive = [a for a in numbers if a >= 0]
negative = [b for b in numbers if b < 0]
even = [e for e in numbers if e % 2 == 0]
odd = [o for o in numbers if o % 2 != 0]

print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')
