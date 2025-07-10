import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    root = int(math.isqrt(N))
    print(1 if root * root == N else 0)
