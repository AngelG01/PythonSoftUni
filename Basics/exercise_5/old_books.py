favourite_book = input()
current_book = input()
checked = 0

found = False
while current_book != favourite_book:
    current_book = input()
    checked += 1
    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {checked} books.")
        break
else:
    print(f"You checked {checked} books and found it.")


