def fibonacci(n):
    count = int(n)
    sequence = [0, 1]

    for i in range(0,count-2):
        result = sequence[i] + sequence[i+1]
        sequence.append(result)
    return sequence

