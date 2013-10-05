def is_prime(i):
    for div in range(2, i):
        if i % div == 0:
            return False
    return True


def primes(N=100):
    res = []
    for i in range(2, N + 1):
        if is_prime(i):
            res.append(i)
    return res


if __name__ == "__main__":
    print(primes())
