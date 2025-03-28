n = int(input())

for _ in range(n):
    a = int(input())
    result = False

    for base in range(2, 65):
        temp = a
        digits = []

        while temp:
            digits.append(temp % base)
            temp //= base

        if digits == digits[::-1]:
            result = True
            break

    print(1 if result else 0)
