f_number = int(input())
s_number = int(input())
t_number = int(input())

numbers = [f_number, s_number, t_number]


def min_number():
    min_number = min(numbers)
    return min_number

print(min_number())