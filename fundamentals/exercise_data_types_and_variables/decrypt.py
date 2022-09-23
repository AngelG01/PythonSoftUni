key = int(input())
length = int(input())
message = ""
for i in range(length):
    letter = input()
    decrypted_letter = ord(letter)
    new_letter = decrypted_letter + key
    message += chr(new_letter)
print(message)
