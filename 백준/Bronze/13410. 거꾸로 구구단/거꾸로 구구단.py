n, k  = map(int, input().split())
re = []

for i in range(1, k+1):
    re.append(int(str(n*i)[::-1]))

print(max(re))