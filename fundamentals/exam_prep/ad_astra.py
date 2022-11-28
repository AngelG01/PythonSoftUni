import re

text = input()
pattern = r'(#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<exp_date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1'
matches = re.finditer(pattern, text)
total_calories = 0
food_data = []
for calories in matches:
    food_data.append(calories.groupdict())
    curr_calories = int(calories.group(4))
    total_calories += curr_calories

days_to_eat = total_calories // 2000
print(f'You have food to last you for: {days_to_eat} days!')

for element in food_data:
    print(f"Item: {element['item']}, Best before: {element['exp_date']}, Nutrition: {element['calories']}")