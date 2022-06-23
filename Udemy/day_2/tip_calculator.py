print("Welcome to tip calculator!")
bill = float(input("What was the bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total = bill + (bill * (percentage / 100))
split = total / people

print(f"Each person should pay: ${split:.2f}")