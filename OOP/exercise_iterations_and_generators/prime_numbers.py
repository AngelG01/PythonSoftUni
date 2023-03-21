def get_primes(integers: list):
    for el in integers:
        is_prime = True
        if el == 1 or el <= 0:
            is_prime = False
            break
        for i in range(2, el):

            if el % i == 0:
                is_prime = False
                break

        if is_prime:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
