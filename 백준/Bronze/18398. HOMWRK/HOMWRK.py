a = int(input())
for i in range(a):
    b = int(input())
    for j in range(b):
        a, b = map(int, input().split())
        print(a+b, a*b)