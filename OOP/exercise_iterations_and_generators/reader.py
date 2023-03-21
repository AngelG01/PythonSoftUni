def read_next(*args):
    for el in args:
        for char in el:
            yield char


for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
