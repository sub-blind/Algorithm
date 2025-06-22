a = int(input())
b = 0

for _ in range(a):
    if int(input()) == 1:
        b += 1

if b > a//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")