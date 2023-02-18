def shop_from_grocery_list(budget, to_buy, *args):
    dict_to_buy = {}

    for el in to_buy:
        if el not in dict_to_buy.keys():
            dict_to_buy[el] = 0

    for element in args:
        product = element[0]
        price = element[1]

        if product in dict_to_buy.keys():
            if dict_to_buy[product] == 0:
                if budget - price >= 0:
                    budget -= price
                    dict_to_buy[product] += 1
                else:
                    break
    left_to_buy = []
    finished = True

    for pr, v in dict_to_buy.items():
        if v == 0:
            left_to_buy.append(pr)
            finished = False
    if finished:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f'You did not buy all the products. Missing products: {", ".join(left_to_buy)}.'


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
