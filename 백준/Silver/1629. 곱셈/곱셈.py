import sys

a, b, c = map(int, sys.stdin.readline().split())


def solve(a, b, c): 
    if b == 1:
        return a % c
    else:
        d = solve(a, b // 2, c)
        if b % 2 == 0:
            return (d * d) % c
        else:
            return (d * d * a) % c


print(solve(a, b, c))