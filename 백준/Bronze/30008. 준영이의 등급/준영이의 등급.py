N, K = map(int, input().split())
G = list(map(int, input().split()))
ranges = [4, 11, 23, 40, 60, 77, 89, 96, 100]
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []
for i in G:
    P = (i * 100) // N
    for j, limit in enumerate(ranges):
        if P <= limit:
            result.append(grades[j])
            break

print(" ".join(map(str, result)))
