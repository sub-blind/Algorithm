import math

def is_square(n):
    return int(math.isqrt(n))**2 == n

def min_squares(n):
    if is_square(n):
        return 1

    for i in range(1, int(math.isqrt(n)) + 1):
        if is_square(n - i*i):
            return 2

    while n % 4 == 0:
        n //= 4
    if n % 8 != 7:
        return 3

    return 4

n = int(input())
print(min_squares(n))
