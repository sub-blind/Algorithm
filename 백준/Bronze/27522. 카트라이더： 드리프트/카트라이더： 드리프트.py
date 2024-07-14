import sys
input = sys.stdin.readline
score = []
point = [10, 8, 6, 5, 4, 3, 2, 1]
r, b = 0, 0
for _ in range(8):
    time, team = input().split()
    score.append((time, team))
score.sort() # 시간으로 비교하더라.

for i in range(8):
    time, team = score[i]
    if team == 'R':
        r += point[i]
    else:
        b += point[i]

print('Red' if r > b else 'Blue')