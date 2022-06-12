count_of_groups = int(input())

musala = 0
monblan = 0
cilimadzharo = 0
k2 = 0
everest = 0

total = 0

for i in range(0, count_of_groups):
    count_of_people = int(input())

    if 0 < count_of_people <= 5:
        musala += count_of_people

    elif 6 <= count_of_people <= 12:
        monblan += count_of_people

    elif 13 <= count_of_people <= 25:
        cilimadzharo += count_of_people

    elif 26 <= count_of_people <= 40:
        k2 += count_of_people

    else:
        everest += count_of_people

    total += count_of_people

musala = musala / total * 100
print(f"{musala:.2f}%")

monblan = monblan / total * 100
print(f"{monblan:.2f}%")

cilimadzharo = cilimadzharo / total * 100
print(f"{cilimadzharo:.2f}%")

k2 = k2 / total * 100
print(f"{k2:.2f}%")

everest = everest / total * 100
print(f"{everest:.2f}%")
