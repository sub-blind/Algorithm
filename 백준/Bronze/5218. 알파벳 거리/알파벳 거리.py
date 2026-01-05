import sys

for _ in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    print("Distances:", end='')
    for x, y in zip(a, b):
        print(f" {(ord(y) - ord(x) + 26) % 26}", end='')
    print()