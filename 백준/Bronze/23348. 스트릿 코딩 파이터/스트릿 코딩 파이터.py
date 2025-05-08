import sys
input = sys.stdin.readline

level = list(map(int, input().split()))
n = int(input())
grades = []

for _ in range(n):
    grade = 0
    for _ in range(3):
        a = list(map(int, input().split()))
        grade += sum(x * y for x, y in zip(a, level))
    grades.append(grade)

print(max(grades))
