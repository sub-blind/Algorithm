num = int(input())

for _ in range(num):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print("Possible")
    else:
        print("Impossible")