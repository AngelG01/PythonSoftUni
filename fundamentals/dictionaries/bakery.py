information = input().split()
bakery = {}


def into_dictionary(information_spliter):
    for piece_info in range(0, len(information_spliter), 2):
        key = information_spliter[piece_info]
        info = information_spliter[piece_info + 1]
        bakery[key] = int(info)


into_dictionary(information_spliter=information)
print(bakery)