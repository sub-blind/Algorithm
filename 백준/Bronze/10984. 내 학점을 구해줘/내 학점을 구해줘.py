import sys
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    n = int(input())
    total_credit = 0
    total_score = 0.0
    for _ in range(n):
        credit, grade = input().split()
        credit = int(credit)
        total_credit += credit
        total_score += credit * float(grade)
    gpa = total_score / total_credit
    results.append(f"{total_credit} {gpa:.1f}")

print("\n".join(results))
