gifts = input().split()
command = input().split()
end = ["No", "Money"]
while command != end:
    if command[0] == "OutOfStock":
        count = gifts.count(command[1])
        for i in range(count):
            if gifts.__contains__(command[1]):
                gifts.remove(command[1])
    elif command[0] == "Required":
        if int(command[2]) <= len(gifts):
            index = int(command[2]) - 1
            gifts.remove(gifts[index])
            gifts.insert(index, command[1])

    elif command[0] == "JustInCase":
        last_value = gifts[-1]
        gifts.remove(last_value)
        gifts.append(command[1])

    command = input().split()

print(" ".join(gifts))
