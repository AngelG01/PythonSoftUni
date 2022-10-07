text = input()
repetitions = int(input())


def manipulation(a: str, b: int):
    repeat_string = lambda a, b: a * b

    result = repeat_string(text, repetitions)
    return result


print(manipulation(text, repetitions))
