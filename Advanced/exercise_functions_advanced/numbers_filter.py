def even_odd_filter(**numbers_to_filter):
    numbers_dict = sorted(numbers_to_filter.items(),
                          key=lambda x: -len(x[1]))
    result = {}
    for type_of_list, value in numbers_dict:
        if type_of_list == 'even':
            result[type_of_list] = [int(x) for x in value if x % 2 == 0]
        else:
            result[type_of_list] = [int(x) for x in value if x % 2 != 0]
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
