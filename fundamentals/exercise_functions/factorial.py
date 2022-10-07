f_num = int(input())
s_num = int(input())


def factorial(number):
    factorial_ = 1
    for i in range(1, number):
        factorial_ *= i
    final = factorial_ * number
    return final


factorial_f = factorial(f_num)
factorial_s = factorial(s_num)
total = factorial_f / factorial_s

print(f'{total:.2f}')
