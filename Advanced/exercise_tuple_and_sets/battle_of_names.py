even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):

    ascii_sum_of_letters = sum(ord(letter) for letter in input()) // row

    if ascii_sum_of_letters % 2 == 0:
        even_set.add(ascii_sum_of_letters)
    else:
        odd_set.add(ascii_sum_of_letters)

if set(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')

# INPUT:
# 4
# Pesho
# Stefan
# Stamat
# Gosho
# -------
#
# 6
# Preslav
# Gosho
# Ivan
# Stamat
# Pesho
# Stefan
