def even_parameters(add):
    def wrapper(*args):
        digits = all(type(ele) != str for ele in args)
        if not digits:
            return f'Please use only even numbers!'
        even = all(el % 2 == 0 for el in args)
        if even and digits:
            return add(*args)
        else:
            return f'Please use only even numbers!'

    return wrapper
