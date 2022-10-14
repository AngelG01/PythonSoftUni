number_of_wagons = int(input())
command = input().split()
wagon_list = [0] * number_of_wagons
while command[0] != 'End':
    if command[0] == "add":
        wagon_list[-1] += int(command[1])
    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        wagon_list[index] -= people

    command = input().split()

print(wagon_list)
