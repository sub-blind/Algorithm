N = int(input())
lis = []

for i in range(N):
    number = int(input())
    lis.append(number)

a = lis[0]
b = max(lis)

if a >= b:
    print("S")
else:
    print("N")
