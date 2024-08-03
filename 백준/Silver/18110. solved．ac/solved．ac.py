import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])

def rounds(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if N == 0:
    print(0)
else:
    scores = [int(data[i]) for i in range(1, N + 1)]
    scores.sort()
    
    trimmed_count = rounds(N * 0.15)
    if trimmed_count != 0:
        scores = scores[trimmed_count:-trimmed_count]
    trimmed_mean = sum(scores) / len(scores)
    print(rounds(trimmed_mean))
