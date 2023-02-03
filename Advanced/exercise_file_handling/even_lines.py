try:
    with open('text.txt', 'r') as file:
        data = file.readlines()

    symbols = ["-", ",", ".", "!", "?"]

    edited_sentences = []

    for index in range(len(data)):
        sentence = data[index].split()[::-1]
        if index % 2 == 0:
            edited_sentences.append(" ".join(sentence))

    for current in range(len(edited_sentences)):
        for char in symbols:
            edited_sentences[current] = edited_sentences[current].replace(char, '@')

    [print(element) for element in edited_sentences]
except FileNotFoundError:
    print('File was not found or path is incorrect.')
