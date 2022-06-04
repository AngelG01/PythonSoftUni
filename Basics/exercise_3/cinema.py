movie_type = input()
rolls = int(input())
columns = int(input())

total_places = rolls * columns
price = 0

if movie_type == "Premiere":
    price = 12
elif movie_type == "Normal":
    price = 7.5
elif movie_type == "Discount":
    price = 5

total_price = total_places * price

print(f"{total_price:.2f} leva")