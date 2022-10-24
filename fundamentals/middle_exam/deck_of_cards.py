cards = input().split(', ')
number = int(input())

for i in range(number):
    command = input().split(', ')
    if command[0] == 'Add':
        card = command[1]
        if card not in cards:
            cards.append(card)
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif command[0] == 'Remove':
        card = command[1]
        if card in cards:
            cards.remove(card)
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command[0] == 'Remove At':
        index = int(command[1])
        if 0 <= index < len(cards):
            cards.remove(cards[index])
            print('Card successfully removed')
        else:
            print('Index out of range')
    elif command[0] == 'Insert':
        index = int(command[1])
        card_name = command[2]
        if not 0 <= index < len(cards):
            print('Index out of range')
            continue
        if card_name in cards:
            print('Card is already added')
            continue
        cards.insert(index, card_name)
        print('Card successfully added')

print(', '.join(cards))
