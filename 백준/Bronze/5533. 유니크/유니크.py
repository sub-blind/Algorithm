N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

count_0 = {}
count_1 = {}
count_2 = {}

for person in data:
    a, b, c = person
    count_0[a] = count_0.get(a, 0) + 1
    count_1[b] = count_1.get(b, 0) + 1
    count_2[c] = count_2.get(c, 0) + 1

for person in data:
    score = 0
    a, b, c = person
    if count_0[a] == 1:
        score += a
    if count_1[b] == 1:
        score += b
    if count_2[c] == 1:
        score += c
    print(score)
