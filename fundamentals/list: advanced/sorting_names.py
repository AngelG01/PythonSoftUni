names = input().split(', ')


def sorting_by_length(names):
    result = sorted(names, key=lambda x: (-len(x), x))
    return result


print(sorting_by_length(names))
