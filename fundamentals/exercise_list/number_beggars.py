number_list = [int(x) for x in input().split(", ")]
number_of_beggars = int(input())

beggars_list = [0] * number_of_beggars

if number_of_beggars == 0:
    print(beggars_list)
    exit()
for current_beggar in range(len(number_list)):
    for n in range(len(number_list)):
        current_number = n % number_of_beggars
        if current_number == current_beggar:
            beggars_list[current_number] += number_list[n]

print(beggars_list)
