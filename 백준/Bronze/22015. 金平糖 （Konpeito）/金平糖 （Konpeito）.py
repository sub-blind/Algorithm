A, B, C = map(int, input().split())

result = max([A, B, C])*3 - sum([A, B, C])
print(result)