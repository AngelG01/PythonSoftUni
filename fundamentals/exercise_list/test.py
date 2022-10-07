cards = input().split()
number_of_shuffles = int(input())
help_deck = []
new_deck = [""] * (len(cards) - 2)
last_index = len(cards)
for card in range(1, len(cards) - 1):
    help_deck.append(cards[card])

for current_card in range(0, len(help_deck)):
    card_new_position = current_card + number_of_shuffles

    if card_new_position >= len(help_deck):
        card_new_position %= len(help_deck)
        new_deck[card_new_position] += help_deck[current_card]
    else:
        new_deck[card_new_position] += help_deck[current_card]

almost_final_deck = [cards[0]]
for element in range(0, len(new_deck)):
    almost_final_deck.append(new_deck[element])
final_deck = []
for sd in range(len(almost_final_deck)):
    final_deck.append(almost_final_deck[sd])
final_deck.append(cards[len(cards) - 1])
print(final_deck)
