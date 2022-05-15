pen = int(input())
markers = int(input())
liters_soup = int(input())
percent_discount = int(input())

pen_price = float(5.8 * pen)
markers_price = float(7.2 * markers)
price_per_liter = float(1.2 * liters_soup)

total_price = (pen_price + markers_price + price_per_liter)
discounted_price = total_price - (total_price*(percent_discount/100))
print(discounted_price)
