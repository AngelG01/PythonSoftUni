def add_songs(*args):
    output = {}
    for element in args:
        song = element[0]
        lyrics = element[1]
        if song not in output.keys():
            output[song] = []
        output[song].extend(lyrics)
    final_string = []

    for key, value in output.items():
        final_string.append(f'- {key}')
        if value:
            final_string.extend(value)

    return '\n'.join(final_string)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
