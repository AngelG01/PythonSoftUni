import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    for_min = arr.copy()
    min_values = []
    for i in range(4):
        min_values.append(min(for_min))
        for_min.remove(min(for_min))
    for_max = arr.copy()
    max_values = []
    for k in range(4):
        max_values.append(max(for_max))
        for_max.remove(max(for_max))
    return f'{sum(min_values)} {sum(max_values)}'


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(miniMaxSum(arr))
