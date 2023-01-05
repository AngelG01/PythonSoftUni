weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

weather_f = {day: (temp_c * 1.8) + 32 for (day, temp_c) in weather_c.items()}

for day, temp_f in weather_f.items():
    print(f'{day}: {temp_f:.1f}')