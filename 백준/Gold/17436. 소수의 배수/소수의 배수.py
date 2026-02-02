def solve():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = 0

    for mask in range(1, 1 << n):
        multiplied = 1
        selected = 0

        for idx in range(n):
            if mask & (1 << idx):
                multiplied *= numbers[idx]
                selected += 1
                if multiplied > m:
                    break

        if multiplied > m:
            continue

        if selected % 2 == 1:
            answer += m // multiplied
        else:
            answer -= m // multiplied

    print(answer)

solve()
