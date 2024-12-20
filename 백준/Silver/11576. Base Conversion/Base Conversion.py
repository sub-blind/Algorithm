import sys

a, b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
digits = list(map(int, sys.stdin.readline().split()))

num = sum(d * (a ** idx) for idx, d in enumerate(digits[::-1]))

converted = []
while num > 0:
    converted.append(num % b)
    num //= b

print(" ".join(map(str, converted[::-1])))
