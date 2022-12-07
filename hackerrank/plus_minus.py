import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = 0
    negative = 0
    neutral = 0
    for current in arr:

        if current > 0:
            positive += 1
        elif current < 0:
            negative += 1
        else:
            neutral += 1

    return f'{(positive / len(arr)):.6f}\n{(negative / len(arr)):.6f}\n{(neutral / len(arr)):.6f}'


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(plusMinus(arr))
