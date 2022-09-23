n = int(input())
to_check = ""
opened_counter = 0
closed_counter = 0
flag = False

for i in range(n):
    text = input()
    to_check += text

for char in to_check:
    start = to_check.index(char)
    if char == "(":
        opened_counter += 1
    if char == ")":
        closed_counter += 1
    if closed_counter > 0 and opened_counter > 0:
        if char == "(" or char == ")":
            for opened in range(start, len(to_check)):
                closed_bracket = to_check.index(")")
                opened_bracket = to_check.index("(")
                nested = to_check[opened]
                if closed_bracket < opened_bracket:
                    flag = True
                if nested == "(":
                    flag = True

if opened_counter != closed_counter:
    flag = True

if flag:
    print("UNBALANCED")
else:
    print("BALANCED")
