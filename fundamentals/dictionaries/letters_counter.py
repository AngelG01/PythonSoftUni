sentence = 'What is the Airspeed Velocity of an Unladen Swallow?'

words = sentence.split(' ')

letters = {word: len(word) for word in words}

for word, length in letters.items():
    print(f'{word}: {length},')
