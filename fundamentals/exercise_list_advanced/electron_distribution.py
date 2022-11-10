electrons = int(input())

filled_shells = []


def electron_shells(electron):
    return lambda n: 2 * n ** 2


for electron in range(1, electrons):
    result = electron_shells(electron)
    if sum(filled_shells) < electrons:
        filled_shells.append(result(electron))
    elif sum(filled_shells) > electrons:
        filled_shells.pop()
        last_electron = electrons - sum(filled_shells)
        filled_shells.append(last_electron)
        continue


print(filled_shells)