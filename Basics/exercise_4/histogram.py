n = int(input())

times1 = 0
times2 = 0
times3 = 0
times4 = 0
times5 = 0

for count in range(1, n + 1):
    number_to_check = int(input())
    if number_to_check < 200:
        times1 += 1

    elif 200 <= number_to_check < 400:
        times2 += 1

    elif 400 <= number_to_check < 600:
        times3 += 1

    elif 600 <= number_to_check < 800:
        times4 += 1

    elif 800 <= number_to_check < 1001:
        times5 += 1

p1 = times1 / n * 100
p2 = times2 / n * 100
p3 = times3 / n * 100
p4 = times4 / n * 100
p5 = times5 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")




