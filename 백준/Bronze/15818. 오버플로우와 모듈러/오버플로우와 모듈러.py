N, M = map(int, input().split())
li = list(map(int, input().split()))
a = 1
for n in li:
    a *= n
print(a%M)