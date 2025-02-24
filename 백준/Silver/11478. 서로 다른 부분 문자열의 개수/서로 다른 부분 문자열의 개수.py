n = input()
result = set()
for i in range(0, len(n)):
    for j in range(i, len(n)):
        result.add(n[i:j+1])
print(len(result))