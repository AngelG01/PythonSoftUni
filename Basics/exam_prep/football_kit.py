tshirt_price = float(input())
price_needed = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (tshirt_price + shorts_price) * 2
price = shoes_price + socks_price + shorts_price +tshirt_price

final_price = price - (price * 0.15)
diff_price = price_needed - final_price
if final_price >= price_needed:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff_price:.2f} lv. more.")