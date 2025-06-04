def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

numbers = [i for i in range(0, 20)]

primeList = list(filter(lambda x: is_prime(x), numbers))
print(primeList)