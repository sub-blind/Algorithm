import sys
N = int(input())
arr = [0] * 10001

for _ in range(N):
    numlist = int(sys.stdin.readline())
    arr[numlist] +=1    
    
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)