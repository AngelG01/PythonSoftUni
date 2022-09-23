rotations = int(input())
key_word = input()
non_filtered = []
filtered = []
for i in range(rotations):
    sentence = input()
    non_filtered.append(sentence)
for sentences in range(len(non_filtered)):
    element = non_filtered[sentences]
    if key_word in element:
        filtered.append(element)
print(non_filtered)
print(filtered)
