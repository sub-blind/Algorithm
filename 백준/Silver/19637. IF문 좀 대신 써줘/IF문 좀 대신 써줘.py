import sys
input = sys.stdin.read

data = input().splitlines()

rankn, n = map(int, data[0].split())

all_ranks = [line.split() for line in data[1:rankn + 1]]

results = []
for i in range(rankn + 1, rankn + n + 1):
    tmp = int(data[i])
    left, right = 0, rankn - 1
    while left <= right:
        mid = (left + right) // 2
        mid_score = int(all_ranks[mid][1])
        if tmp > mid_score:
            left = mid + 1
        else:
            right = mid - 1
    results.append(all_ranks[left][0])
sys.stdout.write("\n".join(results) + "\n")
