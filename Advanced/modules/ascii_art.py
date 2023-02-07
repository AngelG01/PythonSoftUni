from pyfiglet import figlet_format


def convert_to_art(text):
    result = figlet_format(text)
    return result


text = input()

print(convert_to_art(text))
