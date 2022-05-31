fruit = input()
day = input()
quantity = float(input())

day_is_invalid = True
fruit_is_invalid = False
price = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    day_is_invalid = False
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
    else:
        fruit_is_invalid = True

elif day == "Saturday" or day == "Sunday":
    day_is_invalid = False
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2
    else:
        fruit_is_invalid = False

else:
    print("error")

if day_is_invalid == False:
    if fruit_is_invalid == False:
      print(f"{quantity * price:.2f}")
    else:
      print("error")


