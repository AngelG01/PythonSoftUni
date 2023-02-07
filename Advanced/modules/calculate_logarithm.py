from math import log


def log_calc(number, base):
    if base == 'natural':
        return f'{log(number):.2f}'
    else:
        return f'{log(number, int(base)):.2f}'


number = int(input())
base = input()

print(log_calc(number, base))