N = 100

for i in range(2, N + 1):
    is_prime = True
    for div in range(2, i):
        if i % div == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

for i in range(2, N + 1):
    for div in range(2, i):
        if i % div == 0:
            is_prime = False
            break
    else:
        print(i)
