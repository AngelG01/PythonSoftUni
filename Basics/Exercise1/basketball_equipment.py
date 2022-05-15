one_year_tax = int(input())

sneakers_price = (one_year_tax - (one_year_tax * 0.4))
kit_price = (sneakers_price - (sneakers_price * 0.2))
basketball_ball_price = (kit_price * 0.25)
accessories = (basketball_ball_price * 0.2)

print(sneakers_price + kit_price + basketball_ball_price + accessories + one_year_tax)
