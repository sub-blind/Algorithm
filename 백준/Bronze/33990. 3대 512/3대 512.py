n = int(input())
totals = []

for _ in range(n):
    a, b, c = map(int, input().split())
    total = a + b + c
    if total >= 512:
        totals.append(total)

if not totals:
    print(-1)
else:
    min_total = totals[0]
    for total in totals:
        if total - 512 < min_total - 512:
            min_total = total
    print(min_total)