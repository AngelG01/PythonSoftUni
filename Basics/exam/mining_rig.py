from math import ceil
gpu_price = int(input())
connector_price = int(input())
electricity_price = float(input())
earn_per_day = float(input())

total_gpu_price = gpu_price * 13
total_connector_price = connector_price * 13
total_spent = total_connector_price + total_gpu_price + 1000

profit = earn_per_day - electricity_price
profit_per_day = profit * 13

days_to_profit = ceil(total_spent/ profit_per_day)

print(f"{total_spent:.0f}")
print(f"{days_to_profit:.0f}")


