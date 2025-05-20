n = int(input())
scores = [int(input()) for _ in range(n)]

count = 0
for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        count += scores[i] - scores[i + 1] + 1
        scores[i] = scores[i + 1] - 1

print(count)
