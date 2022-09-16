count = int(input())

for number in range(count):
    text = input()
    if text.__contains__(",") or text.__contains__(".") or text.__contains__("_"):
        print(f"{text} is not pure!")

    else:
        print(f"{text} is pure.")
