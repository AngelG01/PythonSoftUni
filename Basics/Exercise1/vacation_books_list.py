current_pages = int(input())
pages_per_hour = int(input())
days = int(input())

days_needed = current_pages// pages_per_hour
hours_per_day = days_needed // days
print(hours_per_day)