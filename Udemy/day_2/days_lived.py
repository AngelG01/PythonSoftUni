age = int(input("What is your current age: "))

days_lived = age * 365
days_left = 90 * 365 - days_lived
weeks_lived = age * 52
weeks_left = 90 * 52 - weeks_lived
months_lived = age * 12
months_left = 90 * 12 - months_lived

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")

# for row in range(0, days_left):
#     for column in range(0, days_left):
#         counter += 1
#         if counter <= days_lived:
#             print("*", end=" ")
#         else:
#             print("-", end=" ")
#     print()
