def forecast(*args):
    data = {}
    for curr in args:
        location, weather = curr[0], curr[1]

        if location not in data.keys():
            data[location] = weather
    sorted_data = sorted(data.items(),
                         key=lambda x: (x[1], x[0]))

    sunny = ''
    cloudy = ''
    rainy = ''

    for key, value in sorted_data:
        if value == 'Sunny':
            sunny += f'{key} - {value}\n'
        elif value == 'Cloudy':
            cloudy += f'{key} - {value}\n'
        elif value == 'Rainy':
            rainy += f'{key} - {value}\n'

    return sunny + cloudy + rainy
