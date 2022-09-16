command = input()
double_char = ""
while command != "End":
    double_char = ""
    for letter in command:
        double_char += letter
        double_char += letter

    if command != "SoftUni":
        print(double_char)
    command = input()
