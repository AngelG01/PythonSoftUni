def math_operations(*numbers, **kwargs):
    for curr_number in range(len(numbers)):
        key = list(kwargs.keys())[curr_number % 4]

        if key == 'a':
            kwargs[key] += numbers[curr_number]
        elif key == 's':
            kwargs[key] -= numbers[curr_number]
        elif key == 'd':
            if numbers[curr_number] != 0:
                kwargs[key] /= numbers[curr_number]
        elif key == 'm':
            kwargs[key] *= numbers[curr_number]

    sorted_kwargs = sorted(kwargs.items(),
                           key=lambda x: (-x[1], x[0]))

    return '\n'.join(f'{k}: {v:.1f}' for k, v in sorted_kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
