from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift_amount
                if new_position >= 26:
                    new_position %= 26
            elif direction == "decode":
                new_position = position - shift_amount
                if new_position < 0:
                    new_position %= 26
            new_letter = alphabet[abs(new_position)]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The {cipher_direction}d text is: {cipher_text}")


should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)
    print()
    restart = input("Do you want to restart? yes/no \n")

    if restart == "no":
        should_end = True
        print("Goodbye!")

