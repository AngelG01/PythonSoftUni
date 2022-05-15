nylon = int(input())
paint = int(input())
diluent = int(input())
hours_for_the_job = int(input())

nylon_price = float((nylon + 2) * 1.5)
paint_price = float((paint + (paint * 0.1)) * 14.5)
diluent_price = float(diluent * 5)

total_price = nylon_price + paint_price + diluent_price + 0.40
end_price = total_price+ ((total_price * 0.3) * hours_for_the_job)

print(end_price)
