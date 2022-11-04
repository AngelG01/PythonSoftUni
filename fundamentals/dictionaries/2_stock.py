information = input().split()
stock = {}

for element in range(0, len(information), 2):
    key = information[element]
    quantity = information[element + 1]
    stock[key] = int(quantity)

search_words = input().split()

for word in search_words:
    if word in stock:
        print(f"We have {stock[word]} of {word} left")
    else:
        print(f"Sorry, we don't have {word}")


