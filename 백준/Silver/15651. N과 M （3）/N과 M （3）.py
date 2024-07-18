from itertools import product
n, m = map(int, input().split())

numbers = range(1, n + 1)

for perm in product(numbers, repeat=m):
    print(" ".join(map(str, perm)))
