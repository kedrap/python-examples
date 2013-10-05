#N = 100
#for i in range(2, N+1):
#    is_prime = True
#    for div in range(2, i):
#        if i % div == 0:
#            is_prime = False
#        break
#    if is_prime:
#        print(i)


def is_prime(i):
    for div in range(2, i):
        if i % div == 0:
            return False

    return True


def primes(N=100):
    results = []
    for i in range(2, N + 1):
        if is_prime(i):
            results.append(i)

    return results


print(primes(100))