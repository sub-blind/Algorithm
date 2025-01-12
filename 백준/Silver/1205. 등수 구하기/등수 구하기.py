n, score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    rank = list(map(int, input().split()))

    if n == p and rank[-1] >= score:
        print(-1)
    else:
        for i in range(n):
            if rank[i] <= score:
                print(i + 1)
                break
        else:
            print(n + 1)
