N, R = map(int, input().split())
returned = set(map(int, input().split()))

missing = []
for i in range(1, N + 1):
    if i not in returned:
        missing.append(i)

if not missing:
    print("*")
else:
    for m in missing:
        print(m, end=" ")
