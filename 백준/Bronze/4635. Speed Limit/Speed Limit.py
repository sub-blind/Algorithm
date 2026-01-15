import sys

lines = sys.stdin.read().strip().splitlines()
i = 0

while True:
    n = int(lines[i])
    i += 1
    if n == -1:
        break

    total = 0
    prev_time = 0

    for _ in range(n):
        s, t = map(int, lines[i].split())
        i += 1
        total += s * (t - prev_time)
        prev_time = t

    print(f"{total} miles")
