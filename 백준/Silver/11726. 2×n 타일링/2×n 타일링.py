N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    prev2, prev1 = 1, 2
    for i in range(3, N + 1):
        current = (prev1 + prev2) % 10007
        prev2, prev1 = prev1, current

    print(prev1)
