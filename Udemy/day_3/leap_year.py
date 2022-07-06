year = int(input())
leap_year = False
if year % 4 == 0:
    leap_year = True
elif year % 100 == 0:
    leap_year = False
elif year % 400 == 0:
    leap_year = True

if leap_year:
    print("Its a leap year")
else:
    print("Not a leap year")
