city = input()
sales = float(input())

comission = 0
city_is_valid = False
if city == "Sofia":
    city_is_valid = True
    if 0 <= sales <= 500:
        comission = 0.05
    elif 500 < sales <= 1000:
        comission = 0.07
    elif 1000< sales <= 10000:
        comission = 0.08
    else:
        comission = 0.12
elif city == "Varna":
    city_is_valid = True
    if 0 <= sales <= 500:
        comission = 0.045
    elif 500 < sales <= 1000:
        comission = 0.075
    elif 1000< sales <= 10000:
        comission = 0.1
    else:
        comission = 0.13
elif city == "Plovdiv":
    city_is_valid = True
    if 0 <= sales <= 500:
        comission = 0.055
    elif 500 < sales <= 1000:
        comission = 0.08
    elif 1000< sales <= 10000:
        comission = 0.12
    else:
        comission = 0.145


total = sales * comission
if sales > 0 and city_is_valid == True:
    print(f"{total:.2f}")
else:
    print("error")

