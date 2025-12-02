import sys
input = sys.stdin.readline

def make_sort_key(item):
    name, scores = item
    k, e, m = scores

    return (-k, e, -m, name)

N = int(input())

students = {}
for _ in range(N):
    name, k, e, m = input().split()
    students[name] = (int(k), int(e), int(m))

sorted_students = sorted(students.items(), key=make_sort_key)

for name, _ in sorted_students:
    print(name)
