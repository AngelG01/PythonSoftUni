vacation_price = float(input())
count_of_puzzles = int(input())
count_of_dolls = int(input())
count_of_bears = int(input())
count_of_minions = int(input())
count_of_trucks = int(input())

total_count = count_of_puzzles + count_of_minions + count_of_trucks \
              + count_of_bears + count_of_dolls

money_made = count_of_puzzles * 2.6 + count_of_minions * 8.2 + count_of_trucks * 2 \
             + count_of_bears * 4.1 + count_of_dolls * 3

total_money = money_made - money_made * 0.1

if total_count >= 50:
    total_money = total_money - total_money * 0.25

if total_money >= vacation_price:
    print(f"Yes! {total_money - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total_money:.2f} lv needed.")

