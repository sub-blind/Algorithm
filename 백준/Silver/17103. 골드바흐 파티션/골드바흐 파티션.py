import sys

MAX = 1000000
check = [0] * (MAX + 1)
check[0] = check[1] = 1

primes = []
for i in range(2, MAX + 1):
    if check[i] == 0:
        primes.append(i)
        for j in range(2 * i, MAX + 1, i):
            check[j] = 1

prime_set = set(primes)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0

    for i in primes:
        if i >= N:
            break
        if (N - i) in prime_set and i <= N - i:
            count += 1
    print(count)
