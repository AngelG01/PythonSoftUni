def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': [], }
    validation = False
    for element in args:
        if element != 'Stop':
            key = element[0]
            product = element[1]
            if key in cart.keys():
                validation = True
                if key == 'Pizza' and len(cart[key]) < 4 and product not in cart[key]:
                    cart[key].append(product)
                elif key == 'Soup' and len(cart[key]) < 3 and product not in cart[key]:
                    cart[key].append(product)
                elif key == 'Dessert' and len(cart[key]) < 2 and product not in cart[key]:
                    cart[key].append(product)

        else:
            break

    if not validation:
        return 'No products in the cart!'
    else:
        final_string = ''
        sorted_data = sorted(cart,
                             key=lambda x: (-len(cart[x]), x))
        for key in sorted_data:
            final_string += f'{key}:\n'
            for element in sorted(cart[key]):
                final_string += f' - {element}\n'
        return final_string


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
