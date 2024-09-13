import sys
from itertools import combinations

input = sys.stdin.read
data = input().splitlines()

result = []
for line in data:
    N = line.split()
    if N[0] == "0":
        break
    S = N[1:]
    for c in combinations(S, 6):
        result.append(" ".join(c))
    result.append("")

sys.stdout.write("\n".join(result) + "\n")