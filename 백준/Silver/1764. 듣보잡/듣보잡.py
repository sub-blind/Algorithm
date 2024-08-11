n, m = map(int, input().split())
a = {input() for _ in range(n)}
b = {input() for _ in range(m)}
result = sorted(a & b)

print(len(result))
print("\n".join(result))
