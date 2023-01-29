def kwargs_length(**kwargs):
    dictionary = kwargs
    return len(dictionary.keys())

dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))

dictionary = {}
print(kwargs_length(**dictionary))