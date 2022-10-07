gifts = input().split()
command = input().split()
end = ["No", "Money"]

while command != end:
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = 'None'

    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(gifts):
            index = int(command[2])
            gifts[index] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input().split()

print(" ".join([x for x in gifts if x != 'None']))
