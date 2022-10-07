number = int(input())


def aliquot_sum(number):
    total = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor

    if total == number:
        return True
    else:
        return False


if aliquot_sum(number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
