
n = int(input())
for _ in range(n):
    p, q = map(int, input().split())
    names = []
    for _ in range(p):
        name = input()
        names.append(name)
    sname = set(names)
    count = p - len(sname)
    print(abs(count))
