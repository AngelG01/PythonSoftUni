from math_funcs import math_operator

first_numb, operator, sec_numb = input().split()
result = math_operator(float(first_numb), operator, int(sec_numb))

print(f'{result:.2f}')
