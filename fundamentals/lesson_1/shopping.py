budget = int(input())
command = input()
total = 0

while command != "End":
    money = int(command)
    total += money

    if total > budget:
        print("You went in overdraft!")
        break
    command = input()

if budget >= total:
    print("You bought everything needed.")
