def logged(func):
    func_name = func.__name__

    def wrapper(*args):
        return f'you called {func_name}{args}\nit returned {func(*args)}'

    return wrapper
