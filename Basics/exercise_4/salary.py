count_of_tabs = int(input())
salary = int(input())

for tab in range(1, count_of_tabs + 1):
    site = input()
    if salary > 0:
        if site == "Facebook":
            salary -= 150
        elif site == "Instagram":
            salary -= 100
        elif site == "Reddit":
            salary -= 50

    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
elif salary > 0:
    print(salary)

