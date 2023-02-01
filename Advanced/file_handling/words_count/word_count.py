import re

try:
    with open('words.txt', 'r') as words:
        words_to_check = words.readline().split()

    with open('input.txt', 'r') as input_:
        given_input = re.findall("'?\w+", input_.read())

    final_result = {}

    for word in words_to_check:
        for element in given_input:
            if word == element.lower():
                if word not in final_result.keys():
                    final_result[word] = 0
                final_result[word] += 1

    sorted_final = sorted(final_result.items(),
                          key=lambda x: -x[1])

    with open('other_text_file.txt', 'w') as other_file:
        for k, v in sorted_final:
            text = f'{k}-{v}\n'
            other_file.write(text)

except FileNotFoundError:
    print(f'File not found or path is incorrect')
