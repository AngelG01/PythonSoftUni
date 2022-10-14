# exercise 1

# add = lambda x: x + 15
# print(add(10))
# multiply = lambda x, y: x * y
# print(multiply(10,15))

# exercise 2
# def func_compute(n):
#     return lambda x: x * n
#
#
# result = func_compute(2)
# print(result(15))
# result = func_compute(3)
# print(result(15))
# result = func_compute(4)
# print(result(15))
# result = func_compute(5)
# print(result(15))
# result = func_compute(6)
# print(result(15))

# exercise 3
# tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# tuples.sort(key=lambda x: x[1])
# print(tuples)

# exercise 4

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)

# exercise 5

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
# cubed = list(map(lambda x: x ** 4, numbers))
# print(cubed)

# exercise 6

# def checker(text):
#     return lambda letter: letter == text[0]
#
#
# result = checker('Hello')
# print(result('H'))

