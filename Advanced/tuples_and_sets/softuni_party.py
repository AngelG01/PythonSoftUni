guest_count = int(input())
guests = set()
vip = []
ordinary = []
for _ in range(guest_count):
    guest = input()
    if len(guest) == 8:
        guests.add(guest)

guest_came = input()

while guest_came != 'END':
    if guest_came in guests:
            guests.remove(guest_came)

    guest_came = input()


for person in guests:
    if person[0].isdigit():
        vip.append(person)
    else:
        ordinary.append(person)

vip.sort()
ordinary.sort()

print(len(guests))
for vi in vip:
    print(vi)
for ord in ordinary:
    print(ord)