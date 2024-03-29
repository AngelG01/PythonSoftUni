def multiply(times):
    def decorator(func):
        def wrapper(number):
            new = func(number) * times
            return new

        return wrapper

    return decorator


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
