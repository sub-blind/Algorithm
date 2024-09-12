import sys
n, k = sys.stdin.readline().split()
a= set()

for _ in range(int(n)):
    a.add(sys.stdin.readline().rstrip())

p = len(a)

if k == 'Y':
    print(p)
elif k == 'F':
    print(p//2)
else:
    print(p//3)