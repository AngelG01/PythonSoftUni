from string import punctuation

with open('line_numbers.txt', 'r') as file:
    data = [line.strip() for line in file.readlines()]

output = open('output_2.txt', 'w')
for index in range(1, len(data) + 1, 1):
    letters = 0
    punct_mark = 0
    for char in data[index - 1]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            if char != ' ':
                punct_mark += 1

    output.writelines(f'Line{index}: {data[index - 1]} ({letters})({punct_mark})\n')
output.close()
