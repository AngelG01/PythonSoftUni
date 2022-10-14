command = input().split('-')
notes = [''] * 10

while command[0] != 'End':
    index = int(command[0]) - 1
    note = command[1]
    notes.pop(index)
    notes.insert(index, note)

    command = input().split('-')

# while ('' in notes):
#     notes.remove('')
# sorted_tasks = [i for i in notes if i]
test = [i for i in notes if not i == '']

print(test)
