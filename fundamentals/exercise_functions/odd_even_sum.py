text = input()


def sum_of_even(text):
    even_sum = 0
    for char in text:
        current_number = int(char)

        if current_number % 2 == 0:
            even_sum += current_number
    return even_sum


def sum_of_odd(text):
    odd_sum = 0
    for char in text:
        current_number = int(char)
        if current_number % 2 != 0:
            odd_sum += current_number
    return odd_sum


print(f'Odd sum = {sum_of_odd(text)}, Even sum = {sum_of_even(text)}')


# for char in text:
#     current_number = int(char)
#
#     if current_number % 2 == 0:
#         even_sum += current_number
#     else:
#         odd_sum += current_number