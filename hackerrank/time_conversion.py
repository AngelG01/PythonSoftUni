s = input()
am_or_pm = s[-2:]
if am_or_pm == 'PM':
    hour = int(s[:2])
    if hour == 12:
        print(f'{(s[:-2])}')
        exit()
    hour += 12

    new_time = str(hour) + s[2:-2]
    print(new_time)
else:
    hour = int(s[:2])
    if hour == 12:
        hour = '00'
        midnight = str(hour) + s[2:-2]
        print(midnight)
        exit()
    print(f'{(s[:-2])}')

