def type_check(needed_type):
    def decorator(func):
        def wrapper(num):
            if type(num) == needed_type:
                return func(num)
            else:
                return f'Bad Type'

        return wrapper

    return decorator
