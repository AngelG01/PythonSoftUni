number_of_users = int(input())
usernames = set()
for _ in range(number_of_users):
    username = input()
    usernames.add(username)

[print(user) for user in usernames]

# INPUT:
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
