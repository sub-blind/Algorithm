def divide_hoard(m, n):
    coins = m
    pirates = []

    for _ in range(n):
        share = coins // n
        extra = coins % n
        pirates.append(share + extra)
        coins = (n - 1) * share

    print(" ".join(map(str, pirates)))
    print(coins)

m, n = map(int, input().split())
divide_hoard(m, n)
