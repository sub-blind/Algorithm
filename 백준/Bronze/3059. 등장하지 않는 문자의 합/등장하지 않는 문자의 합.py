a = int(input())

for _ in range(a):
    data = [0] * 27
    b = input()

    for c in b:
        index = ord(c) - 65
        data[index] += 1

    result = 0

    for i in range(26):
        if data[i] == 0:
            result += (i + 65)

    print(result)
