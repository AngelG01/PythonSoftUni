sequence = input().split()

command = input().split()
while command[0] != 'Stop':

    if command[0] == 'Delete':
        index = int(command[1]) + 1

        if index in range(len(sequence)):
            sequence.remove(sequence[index])

    elif command[0] == 'Swap':
        word1 = command[1]
        word2 = command[2]

        if word1 in sequence and word2 in sequence:
            index1 = sequence.index(word1)
            index2 = sequence.index(word2)
            sequence[index1], sequence[index2] = sequence[index2], sequence[index1]

    elif command[0] == 'Put':
        word = command[1]
        index = int(command[2]) - 1

        if index in range(len(sequence)):
            sequence.insert(index, word)

    elif command[0] == 'Sort':
        sequence.sort(reverse=True)
    elif command[0] == 'Replace':
        new_word = command[1]
        old_word = command[2]

        if old_word in sequence:
            index_old = sequence.index(old_word)
            sequence[index_old] = new_word

    command = input().split()
print(' '.join(sequence))
