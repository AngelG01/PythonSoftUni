count_of_people = int(input())
count_of_sleepovers = int(input())
transport_cards = int(input())
museum_tickets = int(input())

price_per_person = count_of_sleepovers * 20 + transport_cards * 1.6 + museum_tickets * 6
total = count_of_people * price_per_person
final_price = total + (total * 0.25)
print(f"{final_price:.2f}")
