def words_sorting(*args):
    words = {}
    total = 0
    for word in args:
        value = 0
        for letter in word:
            value += ord(letter)
        total += value
        words[word] = value
    final_string = []
    if total % 2 == 0:
        sorted_words = sorted(words, key= lambda x: x[0])
        for curr in sorted_words:
            final_string.append(f'{curr} - {words[curr]}')
        return '\n'.join(final_string)
    else:
        sorted_words = sorted(words, key=lambda x: -words[x])
        for curr in sorted_words:
            final_string.append(f'{curr} - {words[curr]}')
        return '\n'.join(final_string)



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
