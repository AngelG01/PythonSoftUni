nickname = input()
password = input()

correct = False

while correct == False:
   password_try = input()
   if password == password_try:
       print(f"Welcome {nickname}!")
       correct = True
