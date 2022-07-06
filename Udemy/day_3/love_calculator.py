your_name = input("What's your name: ")
their_name = input("What's their name: ")

your_name_lower = your_name.lower()
their_name_lower = their_name.lower()

combined_string = your_name_lower + their_name_lower

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is: {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is: {love_score}, you go well together")
else:
    print(f"Your love score is: {love_score}")