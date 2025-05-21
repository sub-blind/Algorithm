a = 0
b, c = map(int, input().split())
for i in range(1, b+1):
    a += str(i).count(str(c))
print(a)