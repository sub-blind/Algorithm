import sys
import math
n=int(input())

for _ in range(n):
    arr=list(map(int, sys.stdin.readline().split()))
    total=0
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            total+=math.gcd(arr[i],arr[j])

    print(total)