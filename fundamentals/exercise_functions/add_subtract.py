f_number = int(input())
s_number = int(input())
t_number = int(input())


def add(f_number: int, s_number: int):
    total = f_number + s_number
    return total


def subtract(add, t_number):
    final = add - t_number
    return final


print(subtract(add(f_number, s_number), t_number))
