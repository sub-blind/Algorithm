n = int(input())
order = list(map(int, input().split()))
line = []

for i in range(n):
    person = i + 1
    position = order[i]
    line.insert(len(line) - position, person)

print(*line)
