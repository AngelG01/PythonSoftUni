number = float(input())

while number < 1 or number > 100:
    number = float(input())

if 1 <= number <= 100:
    print(f"The number {number:.1f} is between 1 and 100")
