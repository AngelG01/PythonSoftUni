def age_assignment(*args, **kwargs):
    result = []
    for key in kwargs:
        for name in args:
            if key == name[0]:
                result.append(f'{name} is {kwargs[key]} years old.')
    result = sorted(result,
                    key=lambda x: x[0])
    return '\n'.join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
