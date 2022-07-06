height = float(input("How tall are you? "))
weight = float(input("What's your weight? "))

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you are under weight.")
elif 18.5 <= bmi < 25:
    print(f"Your bmi is {bmi} and you are normal weight.")
elif 25 <= bmi < 30:
    print(f"Your bmi is {bmi} and you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your bmi is {bmi} and you are obese.")
else:
    print(f"Your bmi is {bmi} and you are clinically obese.")
