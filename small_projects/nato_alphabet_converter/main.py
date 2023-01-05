import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_data_as_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

word = input('Enter a word: ').upper()

for letter in word:
    if letter in nato_data_as_dict:
        print(nato_data_as_dict[letter])
