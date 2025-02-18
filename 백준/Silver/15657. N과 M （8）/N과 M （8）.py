import sys

def backtrack(start, seq):
    if len(seq) == m:
        print(*seq)
        return

    for i in range(start, n):
        seq.append(nums[i])  
        backtrack(i, seq)    
        seq.pop()           

n, m = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))

backtrack(0, [])
