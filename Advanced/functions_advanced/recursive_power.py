def recursive_power(a, b):
    result = 1

    if b == 0:
        return result
    else:
        result = a *recursive_power(a, b-1)
        return result



print(recursive_power(2, 10))
print(recursive_power(10, 100))