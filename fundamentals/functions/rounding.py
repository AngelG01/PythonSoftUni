numbers = list(map(float, input().split()))


def rounding():
    rounded = []
    for i in range(len(numbers)):
        rounded.append(round(numbers[i]))
    return rounded


print(rounding())
